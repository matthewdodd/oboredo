import xml.etree.ElementTree as ET
import mysql.connector
import os

sesdir = os.fsencode('./OBO_XML_72/sessionsPapers')
#oadir = os.fsencode('./OBO_XML_72/ordinarysAccounts')
#rows = ['div0','div1','interp','join','persName','rs','xptr']

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

for filename in os.listdir(sesdir):
    if filename.endswith(".xml"): 
        tree = ET.parse(filename)
        root = tree.getroot()

        for rec in root.iter('div0'):
            print(rec.attrib)
        continue
    else:
        continue

#cnx.close
