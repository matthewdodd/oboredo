CREATE ROLE DBA_TEST WITH PASSWORD 'golf2000';
CREATE DATABASE DBA_TESTING OWNER DBA_TEST;
ALTER ROLE DBA_TEST LOGIN;
\l

psql -p 5450 -U dba_test -d dba_testing

-- RAW TABLES
CREATE TABLE RAW_DIV0 (ID TEXT, DIV0_TYPE TEXT);
CREATE TABLE RAW_DIV1 (ID TEXT, DIV1_TYPE TEXT);
CREATE TABLE RAW_INTERP (INST TEXT, INTERP_TYPE TEXT, VALUE TEXT);
CREATE TABLE RAW_JOIN (RESULT TEXT, TARGETS TEXT);
CREATE TABLE RAW_RS (INST TEXT, RS_TYPE TEXT, VALUE TEXT);

-- DEFINED TABLES
CREATE TABLE PERSON (INST TEXT, SURNAME TEXT, GIVEN TEXT, AGE TEXT, GENDER TEXT, OCCUPATION TEXT);
CREATE TABLE OFFENCE(INST TEXT, OFFENCE_CATEGORY TEXT, OFFENCE_SUBCATEGORY TEXT);
CREATE TABLE VERDICT(INST TEXT, VERDICT_CATEGORY TEXT, VERDICT_SUBCATEGORY TEXT);
CREATE TABLE PUNISHMENT(INST TEXT, PUNISHMENT_CATEGORY TEXT, PUNISHMENT_SUBCATEGORY TEXT);

-- INSERT VALUES INTO TABLE
--- PERSON
INSERT INTO PERSON (INST, SURNAME) SELECT sur.INST
          ,upper(sur.VALUE)
    FROM raw_interp sur
    WHERE sur.INTERP_TYPE = 'surname'
;
UPDATE PERSON
SET GIVEN=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'given') AS subquery
WHERE PERSON.INST=subquery.INST;
UPDATE PERSON
SET AGE=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'age') AS subquery
WHERE PERSON.INST=subquery.INST;
UPDATE PERSON
SET GENDER=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'gender') AS subquery
WHERE PERSON.INST=subquery.INST;
UPDATE PERSON
SET OCCUPATION=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'occupation') AS subquery
WHERE PERSON.INST=subquery.INST;

--- OFFENCE
INSERT INTO OFFENCE (INST, OFFENCE_CATEGORY) SELECT o.INST, o.VALUE
    FROM raw_interp o
    WHERE lower(o.INTERP_TYPE) = 'offencecategory'
;
UPDATE OFFENCE
SET OFFENCE_SUBCATEGORY=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'offenceSubcategory') AS subquery
WHERE OFFENCE.INST=subquery.INST;

--- VERDICT
INSERT INTO VERDICT (INST, VERDICT_CATEGORY) SELECT o.INST, o.VALUE
    FROM raw_interp o
    WHERE lower(o.INTERP_TYPE) = 'verdictcategory'
;
UPDATE VERDICT
SET VERDICT_SUBCATEGORY=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'verdictSubcategory') AS subquery
WHERE VERDICT.INST=subquery.INST;

--- PUNISHMENT
INSERT INTO PUNISHMENT (INST, PUNISHMENT_CATEGORY) SELECT o.INST, o.VALUE
    FROM raw_interp o
    WHERE lower(o.INTERP_TYPE) = 'punishmentcategory'
;
UPDATE PUNISHMENT
SET PUNISHMENT_SUBCATEGORY=subquery.VALUE
FROM (SELECT giv.INST, giv.VALUE from raw_interp giv where giv.INTERP_TYPE = 'punishmentSubcategory') AS subquery
WHERE PUNISHMENT.INST=subquery.INST;






select distinct interp_type from raw_interp;

select 

select result
      ,split_part(targets, ' ', 1) INST
      ,split_part(targets, ' ', 2) OCCUPATION
from RAW_JOIN
where result = 'persNameOccupation';

select j.result
      ,j.targets
      ,split_part(j.targets, ' ', 1) INST
      ,split_part(j.targets, ' ', -1) PLACE
from RAW_JOIN j
where j.result = 'persNamePlace';