import mysql.connector as mysql
import concurrent.futures
import glob, os, datetime, logging

logging.basicConfig(level=logging.DEBUG, filename='map_person_data.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

start = datetime.datetime.now()
logging.info(f'Start time is {start}')

#sql stmts
createPersonTable = "CREATE TABLE oboredo.person(id varchar(60) NOT NULL COMMENT 'unique person identifier' \
						                        ,type varchar(60) COMMENT 'kind of person being referenced' \
                                                ,gender varchar(60) COMMENT 'gender as determined by the courts' \
                                                ,age varchar(60) COMMENT 'age as determined by the courts' \
                                                ,surname varchar(2000) COMMENT 'surname of the person' \
                                                ,given varchar(2000) COMMENT 'given name of the person' \
                                                ,occupation varchar(2000) COMMENT 'occupation as determined by the courts' \
                                                ,PRIMARY KEY (ID)) \
                    COMMENT 'all persons name in court records'"

insertBasePerson = "insert into oboredo.person(id, type) \
                    select pn.id \
                          ,pn.type \
                    from oboredo.raw_persName pn"

surnamePerson = "UPDATE oboredo.person pn \
                 INNER JOIN oboredo.raw_interp i ON pn.id = i.inst \
                 SET pn.surname = i.value \
                 WHERE i.inst = pn.id \
                 and i.type = 'surname'"

givenPerson = "UPDATE oboredo.person pn \
               INNER JOIN oboredo.raw_interp i ON pn.id = i.inst \
               SET pn.surname = i.value \
               WHERE i.inst = pn.id \
               and i.type = 'given'"

genderPerson = "UPDATE oboredo.person pn \
               INNER JOIN oboredo.raw_interp i ON pn.id = i.inst \
               SET pn.surname = i.value \
               WHERE i.inst = pn.id \
               and i.type = 'gender'"

agePerson = "UPDATE oboredo.person pn \
               INNER JOIN oboredo.raw_interp i ON pn.id = i.inst \
               SET pn.surname = i.value \
               WHERE i.inst = pn.id \
               and i.type = 'age'"

occPerson = "UPDATE oboredo.person pn \
               INNER JOIN oboredo.raw_interp i ON pn.id = i.inst \
               SET pn.surname = i.value \
               WHERE i.inst = pn.id \
               and i.type = 'occupation'"

#dbconfig
try:
  cnx = mysql.connect(host="localhost",
            database="oboredo",
            user="root",
            passwd="golf2000",
            port="3306",
            auth_plugin='mysql_native_password',
            autocommit=True,
            connection_timeout=86400)
except mysql.Error as err:
  logging.error(f'MySQL error raised: {err}')
  
cursor = cnx.cursor()
cursor.execute(createPersonTable)
cnx.commit()
logging.info(f'oboredo.person table has been created')
cursor.execute(insertBasePerson)
cnx.commit()
logging.info(f'oboredo.person initial info filled')
cursor.execute(surnamePerson)
cnx.commit()
logging.info(f'oboredo.person surname updated')
cursor.execute(givenPerson)
cnx.commit()
logging.info(f'oboredo.person given name updated')
cursor.execute(genderPerson)
cnx.commit()
logging.info(f'oboredo.person gender updated')
cursor.execute(agePerson)
cnx.commit()
logging.info(f'oboredo.person age updated')
cursor.execute(occPerson)
cnx.commit()
logging.info(f'oboredo.person occupation updated')
cursor.close()
cnx.close()
logging.info(f'connection closed')

end = datetime.datetime.now()
logging.info(f'End time is {end}')
delta = end - start
logging.info(f'Elapsed time is {delta}')