# OBO Redo

This is a reattempt to perform the data work from my Master's Thesis _The Empire of the Old Bailey Online: The Power of Zero_.

## Prerequisites
You will need the following tools/software (versions used if important)

1. Git (2.30.0.2)
2. PostgreSQL (14.4 - v14 implements new split_part() function which allows negative indexing)
3. Python (3.9.1)

## Getting Started

1. Download all of the data yourself from the [University of Sheffield online repository](http://dx.doi.org/10.15131/shef.data.4775434)
    - I have copied the resulting file as listed below:

```bat
$ dir .
 Volume in drive C has no label.
 Volume Serial Number is 3AB7-6089

 Directory of C:\Users\Matthew\projects\oboredo

06/30/2022  05:18 PM    <DIR>          .
02/07/2021  08:35 AM    <DIR>          ..
02/07/2021  08:35 AM                 8 .gitignore
12/29/2021  03:32 PM             4,505 load_xml.py
02/07/2021  08:35 AM    <DIR>          ordinarysAccounts
12/29/2021  03:32 PM    <DIR>          previous
12/29/2021  05:52 PM             4,530 README.md
02/07/2021  08:35 AM    <DIR>          sessionsPapers
               3 File(s)          9,043 bytes
               5 Dir(s)  555,840,692,224 bytes free
```
 
2. You will also need to pre-create the PostgreSQL database and tables to house the XML data:
- I used the GUI when installing PostgreSQL 14.4 and the only thing I changed from the default was the port number: 5432 >> 5450.
- For precreating everything in the database, these commands will suffice:
    - These commands should be run as the 'postgres' superuser:
```sql
CREATE ROLE DBA_TEST WITH PASSWORD 'golf2000';
CREATE DATABASE DBA_TESTING OWNER DBA_TEST;
ALTER ROLE DBA_TEST LOGIN;
\l
```
    - These commands should be run as the 'dba_test' user:
```bat
psql -p 5450 -U dba_test -d dba_testing
```
```sql
CREATE TABLE RAW_DIV0 (ID TEXT, DIV0_TYPE TEXT);
CREATE TABLE RAW_DIV1 (ID TEXT, DIV1_TYPE TEXT);
CREATE TABLE RAW_INTERP (INST TEXT, INTERP_TYPE TEXT, VALUE TEXT);
CREATE TABLE RAW_JOIN (RESULT TEXT, TARGETS TEXT);
CREATE TABLE RAW_RS (INST TEXT, RS_TYPE TEXT, VALUE TEXT);
```
3. Actually gathering the information from all of the *.xml files is tedious, but the fastest way I have found with python is in the [read_soup_processPool.py](./read_soup_processPool.py) file. Be careful though, this uses the `concurrent.futures.ProcessPoolExecutor()` functionality, which "default[s] to the number of processors on the machine [... But, o]n Windows, max_workers must be less than or equal to 61." This work is being performed on a computer that has an AMD Ryzen 9 5950X process, meaning that to Python it has 32 processors. I have manually increased this to use the actual maximum of `max_workers=60`. This is a very CPU and memory intensive script, which can bog down a not as powerful computer or cause the script to crash.
    - Prior to the run, the CPU was sitting between 2% and 4% utilization and RAM in use was at 7.8 GB
    - At peak of run, CPU was sitting between 99% and 100% utilization and RAM in use was at 12 GB
    - Checking the [log file](./logs/read_soup_processPool.log), we see the last line shows: `Total Elapsed time is 0:00:24.442000`
    - This means we have used a significant amount of computational resources, but the time in this new run versus the old MA run is somewhere in the realm of 75 times faster, and is generally a more reliable and better method for handling this kind of data workload
    
## Contributing
Pull requests are acceptable. It is presumed, however, that you will be forking this repository to validate any work I have performed. Should you wish to contribute to this repository, you are welcome to.

## License
Please see the [LICENSE.md](./LICENSE.md)