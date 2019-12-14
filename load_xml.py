#load_xml.py
#tutorial where this began: https://www.datacamp.com/community/tutorials/python-xml-elementtree

import xml.etree.ElementTree as ET
import mysql, glob, os

parent_dir = 'C:/projects/oboredo/OBO_XML_72/sessionsPapers'
#oadir = os.fsencode('C:/projects/oboredo/OBO_XML_72/ordinarysAccounts')
#rows = ['div0','div1','interp','join','persName','rs','xptr']
elements = []

#try:
#  cnx = mysql.connector.connect(host="localhost",
#                                database='employees',
#                                user="root",
#                                passwd="<change_this>")
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#  cnx.close()
#
#cursor = cnx.cursor()

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
  for rec in root.iter('div1'):
    print("div1 attribute is",str(rec.attrib))
  for rec in root.iter('interp'):
    print("interp attribute is",str(rec.attrib))
  for rec in root.iter('xptr'):
    print("xptr attribute is",str(rec.attrib))
  for rec in root.iter('join'):
    print("join attribute is",str(rec.attrib))
  for rec in root.iter('persName'):
    print("persName attribute is",str(rec.attrib))
  for rec in root.iter('rs'):
    print("rs attribute is",str(rec.attrib))

#cnx.close
