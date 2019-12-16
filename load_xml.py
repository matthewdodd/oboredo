#load_xml.py
#tutorial where this began: https://www.datacamp.com/community/tutorials/python-xml-elementtree
#change the passwd at line 27 to your chosen root passwd
#the output file is called "load_xml.log" and can be tailed from a Terminal or Git Bash with the command 'tail -f load_xml.log'
#run time is:
#     started at                    2019-12-15 13:15:47
#     sessionsPapers ended at       2019-12-16 13:51:56
#     ordinarysAccounts ended at    2019-12-16 14:16:22
#     elapsed                       1 day, 1:00:35

import xml.etree.ElementTree as ET
import mysql.connector as mysql
import glob, os, datetime, logging

logging.basicConfig(level=logging.DEBUG, filename='load_xml.log', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

a = datetime.datetime.now()
logging.info('Start time is %s', a)

dirs = ['C:/projects/oboredo/OBO_XML_72/sessionsPapers', 'C:/projects/oboredo/OBO_XML_72/ordinarysAccounts']
#elements = []

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

for parent_dir in dirs:
  for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
    logging.info('XML file being interpreted is %s', xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
  #  for elem in root.iter():
  #    elements.append(elem.tag)
  #    elements = list(dict.fromkeys(elements))
  #    print(elements)
    for rec in root.iter('div0'):
      #print("div0 attribute is",str(rec.attrib))
      div0_sql = "insert into oboredo.raw_div0(type, id) values (%s, %s)"
      div0_val = (str(rec.attrib.get("type")), str(rec.attrib.get("id")))
      cursor.execute(div0_sql, div0_val)
      cnx.commit()
    for rec in root.iter('div1'):
      #print("div1 attribute is",str(rec.attrib))
      div1_sql = "insert into oboredo.raw_div1(type, id) values (%s, %s)"
      div1_val = (str(rec.attrib.get("type")), str(rec.attrib.get("id")))
      cursor.execute(div1_sql, div1_val)
      cnx.commit()
    for rec in root.iter('interp'):
      #print("interp attribute is",str(rec.attrib))
      interp_sql = "insert into oboredo.raw_interp(inst, type, value) values (%s, %s, %s)"
      interp_val = (str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value")))
      cursor.execute(interp_sql, interp_val)
      cnx.commit()
    for rec in root.iter('xptr'):
      #print("xptr attribute is",str(rec.attrib))
      xptr_sql = "insert into oboredo.raw_xptr(type, doc) values (%s, %s)"
      xptr_val = (str(rec.attrib.get("type")), str(rec.attrib.get("doc")))
      cursor.execute(xptr_sql, xptr_val)
      cnx.commit()
    #join is going to be different, some join xml tags don't have everything so we will input default values
    for rec in root.iter('join'):
      #print("join attribute is",str(rec.attrib))
      join_sql = "insert into oboredo.raw_join(result, id, targOrder, targets) values (%s, %s, %s, %s)"
      join_val = (str(rec.attrib.get("result", "unknown")), str(rec.attrib.get("id", "unknown")), str(rec.attrib.get("targOrder", "M")), str(rec.attrib.get("targets", "unknown")))
      cursor.execute(join_sql, join_val)
      cnx.commit()
    for rec in root.iter('persName'):
      #print("persName attribute is",str(rec.attrib))
      persName_sql = "insert into oboredo.raw_persName(id, type) values (%s, %s)"
      persName_val = (str(rec.attrib.get("id")), str(rec.attrib.get("type")))
      cursor.execute(persName_sql, persName_val)
      cnx.commit()
    for rec in root.iter('rs'):
      #print("rs attribute is",str(rec.attrib))
      rs_sql = "insert into oboredo.raw_rs(id, type) values (%s, %s)"
      rs_val = (str(rec.attrib.get("id")), str(rec.attrib.get("type")))
      cursor.execute(rs_sql, rs_val)
      cnx.commit()

cnx.close
logging.warning('cnx is now closed')

b = datetime.datetime.now()
logging.info('End time is %s', b)
delta = b - a
logging.info('Elapsed time is %s', delta)