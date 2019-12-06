import mysql.connector
import os

rows = ['div0','div1','interp','join','persName','rs','xptr']
sesdir = os.fsencode('./OBO_XML_72/sessionsPapers')
oadir = os.fsencode('./OBO_XML_72/ordinarysAccounts')

try:
  cnx = mysql.connector.connect(host="localhost",
                                database='employees',
                                user="root",
                                passwd="<change_this>")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

cursor = cnx.cursor()

for filename in os.listdir(sesdir):
    if filename.endswith(".xml"): 
        for x in rows:
          sql = str("LOAD XML LOCAL INFILE '",filename,"' INTO TABLE oboreda.",x," ROWS IDENTIFIED BY '<",x,">'")
          print(sql)
          #cursor.execute(sql)
          #cnx.commit()
        continue
    else:
        continue

cnx.close
