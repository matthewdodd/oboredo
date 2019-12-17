#load_xml.py
#tutorial where this began: https://www.datacamp.com/community/tutorials/python-xml-elementtree
#change the passwd at line 68 to your chosen root passwd
#the output file is called "load_xml.log" and can be tailed from a Terminal or Git Bash with the command 'tail -f load_xml.log'
#run time is:
#     started at                    
#     sessionsPapers ended at       
#     ordinarysAccounts ended at    
#     elapsed                       

import xml.etree.ElementTree as ET
import mysql.connector as mysql
import glob, os, datetime, logging

logging.basicConfig(level=logging.DEBUG, filename='load_xml.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

a = datetime.datetime.now()
logging.info('Start time is %s', a)

dirs = ['C:/projects/oboredo/OBO_XML_72/sessionsPapers', 'C:/projects/oboredo/OBO_XML_72/ordinarysAccounts']
files = []
div0 = []
div1 = []
interp = []
xptr = []
join = []
persName = []
rs = []

div0_sql = "insert into oboredo.raw_div0(type, id) values (%s, %s)"
div1_sql = "insert into oboredo.raw_div1(type, id) values (%s, %s)"
interp_sql = "insert into oboredo.raw_interp(inst, type, value) values (%s, %s, %s)"
xptr_sql = "insert into oboredo.raw_xptr(type, doc) values (%s, %s)"
join_sql = "insert into oboredo.raw_join(result, id, targOrder, targets) values (%s, %s, %s, %s)"
persName_sql = "insert into oboredo.raw_persName(id, type) values (%s, %s)"
rs_sql = "insert into oboredo.raw_rs(id, type) values (%s, %s)"

for parent_dir in dirs:
  for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    files.append(xml_file)

with files as xf:
    logging.info('XML file being interpreted is %s', xf)
    tree = ET.parse(xf)
    root = tree.getroot()
    for rec in root.iter('div0'):
      div0.append(str(rec.attrib.get("type")), str(rec.attrib.get("id")))
    for rec in root.iter('div1'):
      div1.append(str(rec.attrib.get("type")), str(rec.attrib.get("id")))
    for rec in root.iter('interp'):
      interp.append(str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value")))
    for rec in root.iter('xptr'):
      xptr.append(str(rec.attrib.get("type")), str(rec.attrib.get("doc")))
    #join is going to be different, some join xml tags don't have everything so we will input default values
    for rec in root.iter('join'):
      join.append(str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("id", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown")))
    for rec in root.iter('persName'):
      persName.append(str(rec.attrib.get("id")), str(rec.attrib.get("type")))
    for rec in root.iter('rs'):
      rs.append(val1, val2)str(rec.attrib.get("id")), str(rec.attrib.get("type")))

try:
  cnx = mysql.connect(host="localhost",
                        database="oboredo",
                        user="root",
                        passwd="<change this>",
                        port="3306",
                        auth_plugin='mysql_native_password')
except mysql.Error as err:
  logging.error(f'MySQL error raised: %s', err)

cursor = cnx.cursor()
cursor.execute('SET autocommit = 0')
cnx.commit()

try:
  cursor.executemany(div0_sql, div0)
  cursor.executemany(div1_sql, div1)
  cursor.executemany(interp_sql, interp)
  cursor.executemany(xptr_sql, xptr)
  cursor.executemany(join_sql, join)
  cursor.executemany(persName_sql, persName)
  cursor.executemany(rs_sql, rs)
  cnx.commit
except mysql.Error as err:
  logging.error(f'MySQL error raised: %s', err)

cnx.close
logging.warning('cnx is now closed')

b = datetime.datetime.now()
logging.info('End time is %s', b)
delta = b - a
logging.info('Elapsed time is %s', delta)