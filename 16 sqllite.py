
'''
Creare il DB con il tool sqllite che si carica dal sito :

sqlite3 film.sqlite

https://code.activestate.com/pypm/ per ricercare un oggetto / funzione

pip install iptools

film = tabelle("nometabella", db)


'''

import sqlite3
import iptools

db = sqlite3.connect('./film.sqlite')
db.execute("drop table film")
db.commit()
db.execute("create table film (id INTEGER PRIMARY KEY AUTOINCREMENT, titolo )")
db.commit()
tit=input("metti il titolo del film :")
db.execute("insert into film values (null,'%s')" % (tit))
db.commit()
cursor = db.cursor()
sql1="select * from film"
try:
    cursor.execute(sql1)
    
    res=cursor.fetchall()
    for row in res:
        print(str(row[0])+" "+str(row[1]))
except Exception as e:
    print("got it :-) ", e)


#db.execute("CREATE TABLE ip (id INTEGER PRIMARY KEY AUTOINCREMENT, ip INTEGER)")

#db.commit

class tabella:
    __tabella=""
    
    def __init__(self,tabella):
        self.__tabella=tabella
    def insert(self,valori,db):
        db.execute("insert into %s values (%s)" % valori)
        db.commit()


ip=input("inserisci l'ip : ")
try:
    db.execute( "insert into ip (ip) values ('%d')" % iptools.ipv4.ip2long(ip))
    db.commit()
except Exception as e:
    print("got it :-) ", e)

try:
    cursor.execute("select * from ip")
    
    res=cursor.fetchall()
    for row in res:
        print(str(row[0])+" "+str(iptools.ipv4.long2ip(row[1])))
except Exception as e:
    print("got it :-) ", e)
    
    

db.close()
