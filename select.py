#!/usr/bin/python3
#Importing needed modules of PyMySQL
from pymysql import connect, err, sys, cursors
conn = connect( host = 'localhost',
                        port = 3306,
                        user = 'npMi',
                        passwd = 'bX9wGnXybLsVKxxx',
                        db = 'PN' )
cursor = conn.cursor(cursors.DictCursor)
cursor.execute("SELECT * FROM `TAGIPsql` ")
data = cursor.fetchall()
for row in data:
    print(row['Id'])
    
cursor.close()