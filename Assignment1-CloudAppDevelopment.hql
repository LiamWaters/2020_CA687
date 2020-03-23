
hive
-- View existing tables
SHOW tables;

-- Print column headers
SET hive.cli.print.header=true;

-- Create a table holding the reduced number of columns
CREATE TABLE listings (
provence_name STRING,
country_name STRING,
Last_update TIMESTAMP,
cYear INT,
cMonth INT,
cDay INT,
Confirmed INT,
Deaths INT,
Recovered INT,
Latitude FLOAT,
Longitude FLOAT,
Recorded_Date STRING)
row format delimited 
fields terminated by '|' 
location '/cleansedcoronadata';

select * from listings;

quit;


hive -e 'set hive.cli.print.header=true; select * from listings' | sed 's/[\t]/,/g'  > /home/liam_waters3/assignment1_bigdata_hive_output.csv

gsutil du -s gs://ca687_assignment1_corona/
gsutil cp assignment1_bigdata_hive_output.csv gs://ca687_assignment1_corona/




