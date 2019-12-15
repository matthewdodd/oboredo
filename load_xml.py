#load_xml.py
#tutorial where this began: https://www.datacamp.com/community/tutorials/python-xml-elementtree

import xml.etree.ElementTree as ET
import mysql.connector as mysql
import glob, os

parent_dir = 'C:/projects/oboredo/OBO_XML_72/sessionsPapers'
#oadir = os.fsencode('C:/projects/oboredo/OBO_XML_72/ordinarysAccounts')
#rows = ['div0','div1','interp','join','persName','rs','xptr']
elements = []

try:
  cnx = mysql.connect(host="localhost",
                        database="oboredo",
                        user="root",
                        passwd="<change_this>",
                        port="3306",
                        auth_plugin='mysql_native_password')
except mysql.Error as err:
  print(err)

cursor = cnx.cursor()

for xml_file in glob.glob(os.path.join(parent_dir, '*.xml')):
  print (xml_file)
  tree = ET.parse(xml_file)
  root = tree.getroot()
#  for elem in root.iter():
#    elements.append(elem.tag)
#    elements = list(dict.fromkeys(elements))
#    print(elements)
  for rec in root.iter('div0'):
    print("div0 attribute is",str(rec.attrib))
    div0_sql = "insert into oboredo.raw_div0(type, id) values (%s, %s)"
    div0_val = (str(rec.attrib.get("type")), str(rec.attrib.get("id")))
    cursor.execute(div0_sql, div0_val)
    cnx.commit()
  for rec in root.iter('div1'):
    print("div1 attribute is",str(rec.attrib))
    div1_sql = "insert into oboredo.raw_div1(type, id) values (%s, %s)"
    div1_val = (str(rec.attrib.get("type")), str(rec.attrib.get("id")))
    cursor.execute(div1_sql, div1_val)
    cnx.commit()
  for rec in root.iter('interp'):
    print("interp attribute is",str(rec.attrib))
    interp_sql = "insert into oboredo.raw_interp(inst, type, value) values (%s, %s, %s)"
    interp_val = (str(rec.attrib.get("inst")), str(rec.attrib.get("type")), str(rec.attrib.get("value")))
    cursor.execute(div1_sql, div1_val)
    cnx.commit()
  #for rec in root.iter('xptr'):
  #  print("xptr attribute is",str(rec.attrib))
  #for rec in root.iter('join'):
  #  print("join attribute is",str(rec.attrib))
  #for rec in root.iter('persName'):
  #  print("persName attribute is",str(rec.attrib))
  #for rec in root.iter('rs'):
  #  print("rs attribute is",str(rec.attrib))

#cnx.close
