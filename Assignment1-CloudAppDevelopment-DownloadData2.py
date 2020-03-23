import requests
import shutil
import csv
import os
import datetime;


def callme():

	for x in range(1, 51):
  		xdate = ((datetime.date.today() - datetime.timedelta(days=x)).strftime('%m-%d-%Y'))
		print(xdate)
		url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(xdate)
		print(url)
		r = requests.get(url, verify=False,stream=True)
		if r.status_code!=200:
			print "Failure!!"
			exit()
		else:
			r.raw.decode_content = True
			with open("{}.csv".format(xdate), 'wb') as f:
				shutil.copyfileobj(r.raw, f)
			print "Success"


def calljoin():
	f = open("combined.csv", "w")

	for x in range(1, 51):
  		xdate = ((datetime.date.today() - datetime.timedelta(days=x)).strftime('%m-%d-%Y'))
		append_date = ((datetime.date.today() - datetime.timedelta(days=x)).strftime('%Y-%m-%d'))

		reader = csv.reader(open("/home/liam_waters3/{}.csv".format(xdate)))
		#next(reader, None)

		writer = csv.writer(f)

		for row in reader:
			row.insert(0, append_date)    			
			writer.writerow(row)
	f.close()


def DeDupeOutput():

	with open('/home/liam_waters3/combined.csv','r') as in_file, open('/home/liam_waters3/DedupedCombinedInformation.csv','w') as out_file:
    		seen = set() # set for fast O(1) amortized lookup
    		for line in in_file:
        		if line not in seen: 
           		 	seen.add(line)
            			out_file.write(line)

def DeleteRedundantFiles():

	for x in range(1, 51):
  		xdate = ((datetime.date.today() - datetime.timedelta(days=x)).strftime('%m-%d-%Y'))
		os.remove('/home/liam_waters3/{}.csv'.format(xdate))
	os.remove('/home/liam_waters3/combined.csv')

def LoadintoHadoop():
	os.system('hadoop fs -rm /input/DedupedCombinedInformation.csv')
	os.system('hadoop fs -put /home/liam_waters3/DedupedCombinedInformation.csv /input')




if __name__ == '__main__':
    callme()
    calljoin()
    DeDupeOutput()
    DeleteRedundantFiles()
    LoadintoHadoop()