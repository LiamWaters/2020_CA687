
#import the libraries
from bs4 import BeautifulSoup
import requests
import csv

# this is the url to scrape from.
page_link = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'


#in order to save into a csv file, first I create the file using the command open. csvfile is a variable used to access the file (file handle)
#csvfile = open('memebrs2018.csv', 'w')
csvfile1 = open('corona_age_details.csv', 'w')
csvfile2 = open('corona_sex_details.csv', 'w')
csvfile3 = open('corona_condition_details.csv', 'w')

#get the content from the web and save into the varialbe html_page, using the requests library
html_page = requests.get(page_link, timeout=5)

#parsing the page using BeautifulSoup. The object returned is a strcutured version of the html page
page_content = BeautifulSoup(html_page.content, "html.parser")


#searching for all the tags "table" and save into the varialbe table. 
#table is a list of all the html tables present on the page. In our example we have only one
tables = page_content.find_all("table")

#print the number of tables
####print(len(tables))   #returns 1

#select the first table and save it into the variable mytable
agetable = tables[0]
sextable = tables[1]
conditiontable = tables[2]


#create an object writer to write the csv file. We are telling Python that it is a csv delimited by comma and text with “,” inside are enclosed in quotes
writer1 = csv.writer(csvfile1, delimiter=',',lineterminator='\n',quotechar = '"')
writer2 = csv.writer(csvfile2, delimiter=',',lineterminator='\n',quotechar = '"')
writer3 = csv.writer(csvfile3, delimiter=',',lineterminator='\n',quotechar = '"')

#write a header to the file. This command write the 3 header to the file using the command wrtierow. The input to writerow is a list representing a single row of the csv file
writer1.writerow( ["AGE","DEATH_RATE1","DEATH_RATE2"] )
writer2.writerow( ["SEX","DEATH RATE - confirmed cases","DEATH RATE - all cases"] )
writer3.writerow( ["PRE-EXISTING CONDITION","DEATH RATE - confirmed cases","DEATH RATE - all cases"] )

#loop over the table content

#first I get all the rows (tag <tr>)
trs1 = agetable.find_all("tr")
trs2 = sextable.find_all("tr")
trs3 = conditiontable.find_all("tr")

#loop – this loop takes all the rows one by one
#for each rows it gets all the columns (tag <th> or <td>)
#then save the content of the first column into the variable name, the second into the variable surname and the third into the variable age
#during the loop, I also write to the csv file


for rows in trs1[1:]:

    try:
        cols = rows.find_all(['th', 'td'])   #find all the <th> or <td> columns inside each row
        AGE = cols[0].text
        DEATH_RATE1 = cols[1].text
        DEATH_RATE1 = DEATH_RATE1.strip('\n')
        DEATH_RATE2 = cols[2].text
       
        print(AGE,DEATH_RATE1,DEATH_RATE2)  #print to the screen
    	#write a single line to the file
        writer1.writerow( [AGE,DEATH_RATE1,DEATH_RATE2]  )
    except:
        print(AGE,DEATH_RATE1,DEATH_RATE2)  

#when the loop is done, close the file
csvfile1.close()


for rows in trs2[1:]:

    try:
        cols = rows.find_all(['th', 'td'])   #find all the <th> or <td> columns inside each row
        SEX = cols[0].text
        DEATH_RATE1 = cols[1].text
        DEATH_RATE1 = DEATH_RATE1.strip('\n')
        DEATH_RATE2 = cols[2].text
      
        print(SEX,DEATH_RATE1,DEATH_RATE2)  #print to the screen
    	#write a single line to the file
        writer2.writerow( [SEX,DEATH_RATE1,DEATH_RATE2]  )
    except:
        print(SEX,DEATH_RATE1,DEATH_RATE2)  

#when the loop is done, close the file
csvfile2.close()

for rows in trs3[1:]:

    try:
        cols = rows.find_all(['th', 'td'])   #find all the <th> or <td> columns inside each row
        CONDITION = cols[0].text
        DEATH_RATE1 = cols[1].text
        DEATH_RATE1 = DEATH_RATE1.strip('\n')
        DEATH_RATE2 = cols[2].text
       
        print(CONDITION,DEATH_RATE1,DEATH_RATE2)  #print to the screen
    	#write a single line to the file
        writer3.writerow( [CONDITION,DEATH_RATE1,DEATH_RATE2]  )
    except:
        print(CONDITION,DEATH_RATE1,DEATH_RATE2)  

#when the loop is done, close the file
csvfile3.close()
