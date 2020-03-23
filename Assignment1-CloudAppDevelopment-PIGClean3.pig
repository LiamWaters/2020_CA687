listings = LOAD '/input/DedupedCombinedInformation.csv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','YES_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER')  

AS(Recorded_Date:chararray, provence_name:chararray, country_name:chararray, Last_update:DateTime, Confirmed:int, Deaths:int, Recovered:int, Latitude:float, Longitude:float);



listings = FOREACH listings GENERATE 
		Recorded_Date,
		REPLACE(provence_name,',','-'),
		REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
		country_name,
		'Mainland China','China'),
		'Others','Ships'),
		',','-'),
		'Congo \\(Brazzaville\\)','Republic of the Congo'),
		'Congo \\(Kinshasa\\)','Republic of the Congo'),
		'Gambia, The','Gambia'),
		'Gambia- The','Gambia'),
		'Iran \\(Islamic Republic of\\)','Iran'),
		'Korea- South','South Korea'),
		'occupied Palestinian territory','Palestine'),
		'Republic of Ireland','Ireland'),
		'Taiwan\\*','Taiwan'),
		'The Bahamas','Bahamas'),
		'The Gambia','Gambia'),
		'UK','United Kingdom'),
		'Viet Nam','Vietnam'),
		'Russian Federation','Russia'),
		'North Ireland','United Kingdom'),
		'Hong Kong SAR','Hong Kong'),
		'Holy See','Vatican City'),
		'Bahamas- The','Bahamas'),
		' Azerbaijan','Azerbaijan'),
		Last_update,
		GetYear(Last_update),
		GetMonth(Last_update),
		GetDay(Last_update),
		(Confirmed IS NOT NULL ? Confirmed : 0) as Confirmed,
		(Deaths IS NOT NULL ? Deaths : 0) as Deaths,
		(Recovered IS NOT NULL ? Recovered : 0) as Recovered,
		(Latitude IS NOT NULL ? Latitude : 0) as Latitude,
		(Longitude IS NOT NULL ? Longitude : 0) as Longitude;


/*DUMP listings;*/


STORE listings into '/cleansedcoronadata' USING org.apache.pig.piggybank.storage.CSVExcelStorage('|','NO_MULTILINE','NOCHANGE','SKIP_OUTPUT_HEADER');
