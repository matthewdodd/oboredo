# insert_data.py

import psycopg2
import csv, datetime, logging, os

logging.basicConfig(level=logging.DEBUG, filename='./logs/insert_data.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

start = datetime.datetime.now()
logging.info(f'Start time is {start}')

#word replacement
checkWords = ("Military/Naval","ordinarysAccounts/","sessionsPapers/","/2","/3","/8","/4","/","'")
repWords = ("Military or Naval","ordinarysAccounts-","sessionsPapers-","over two","over three","over eight","over four",""," ")

#sql stmts
div0_sql = "insert into raw_div0(id, div0_type) values"
div1_sql = "insert into raw_div1(id, div1_type) values"
interp_sql = "insert into raw_interp(inst, interp_type, value) values"
join_sql = "insert into raw_join(result, targets) values"
rs_sql = "insert into raw_rs(inst, rs_type, value) values"

def connect(in_sql, in_data, in_arg):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            host="localhost",
            database="dba_testing",
            port=5450,
            user="dba_test",
            password="golf2000")
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        try:
            if in_arg in ['two']:
                argument_string = ",".join("('%s', '%s')" % (x, y) for (x, y, *z) in in_data)
            else:
                argument_string = ",".join("('%s', '%s', '%s')" % (x, y, z) for (x, y, z, *b) in in_data)
            cur.execute(in_sql + argument_string)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as err:
            logging.error(f'Error raised: {err}')
            for row in in_data:
                logging.error(f'Data was: {row} // {len(row)}')
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        logging.error(f'Error raised: {error}')
        for row in in_data:
            logging.error(f'Data was: {row} // {len(row)}')
    finally:
        if conn is not None:
            conn.close()

f1 = open('./output/list_interp.txt', 'r', encoding = "utf-8")
f2 = open('./output/clean_list_interp.txt', 'w', encoding = "utf-8")
for line in f1:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()

f1 = open('./output/list_rs.txt', 'r', encoding = "utf-8")
f2 = open('./output/clean_list_rs.txt', 'w', encoding = "utf-8")
for line in f1:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()

os.remove('./output/list_interp.txt')
os.remove('./output/list_rs.txt')
os.rename('./output/clean_list_interp.txt','./output/list_interp.txt')
os.rename('./output/clean_list_rs.txt','./output/list_rs.txt')

#insert info into database
with open('./output/list_div0.txt', 'r', encoding = "utf-8") as fp:
    file_content = csv.reader(fp)
    connect(div0_sql, file_content, 'two')
    logging.info(f'div0 has completed')

with open('./output/list_div1.txt', 'r', encoding = "utf-8") as fp:
    file_content = csv.reader(fp)
    connect(div1_sql, file_content, 'two')
    logging.info(f'div1 has completed')

with open('./output/list_interp.txt', 'r', encoding = "utf-8") as fp:
    file_content = csv.reader(fp)
    connect(interp_sql, file_content, 'three')
    logging.info(f'interp has completed')

with open('./output/list_join.txt', 'r', encoding = "utf-8") as fp:
    file_content = csv.reader(fp)
    connect(join_sql, file_content, 'two')
    logging.info(f'join has completed')

with open('./output/list_rs.txt', 'r', encoding = "utf-8") as fp:
    file_content = csv.reader(fp)
    connect(rs_sql, file_content, 'three')
    logging.info(f'rs has completed')

end = datetime.datetime.now()
logging.info(f'End time is {end}')
delta = end - start
logging.info(f'Total Elapsed time is {delta}')