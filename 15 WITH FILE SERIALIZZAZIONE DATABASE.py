'''
with

L'istruzione with è usata per inglobare l'esecuzione di un
blocco con metodi definiti da un gestore di contesto e
permette di eseguire le istruzioni contenute nel blocco


with OGGETTO as VARIABILE:
    VARIABILE.metodo


Struttura base :

class DatabaseConnection():
    def __enter__(self):
        # esegue una connessione al database e la restituisce
        ...
        return self.dbconn
    def __exit__(self, type, val, traceback):
        # si assicura che la dbconnection si chiuda
        self.dbconn.close()

with DatabaseConnection() as mydbconn:
     mydbconn.close()



FILE

Tutto ciò vale per file di testo e file binari

output = open('pippo.txt','w')  apertura di un file in scrittura
input = open('dati','r')        apertura di un file in lettura
s = input.read()                lettura dell’intero contenuto del file
s = input.read(N)               lettura di N bytes
s = input.readline()            lettura di una riga (per files di testo)
s = input.readlines()           restuisce l’intero file come lista di righe (per files di testo)
output.write(s)                 scrive nel file i valori passati come parametri e ritorna il numero di bytes scritti
output.writelines(L)            scrive la lista L in righe nel file
output.close(L)                 chiusura del file


Modalità Descrizione
“r”             Apre un file di testo in lettura, equivalente a "rt", se si omette il secondo parametro di open è la modalità di default
“w”             Apre un file in scrittura, e ne azzera i contenuti
“a”             Apre un file in scrittura con il puntatore del file a fine del file
“rb” e “wb”     Apre un file binario in lettura o scrittura con azzeramento del contenuto
“w+” e “w+b”    Aprono un file in modifica, rispettivamente testuale e binario, e consentendone l’aggiornamento, ma ne azzerano i contenuti
“r+” e “r+b”    Aprono un file in modifica, rispettivamente testuale e binario, e ne consentono l’aggiornamento senza azzerare i contenuti


tell()          Ritorna la posizione attuale del cursore all’interno del file
seek(pos, rel)  Sposta la posizione del cursore all’interno del file (se il file è un testo la posizione è in caratteri), con il primo parametro indichiamo il numero di byte (positivo o negativo) di cui vogliamo
                spostarci, il secondo parametro indica il punto di partenza ( 0=dell’inizio del file; 1=dalla posizione attuale; 2:dalla fine del file)
read(N)         Legge N bytes dalla posizione corrente e sposta il cursore avanti di N posizioni



print(miofile) Per verificare lo stato del file 





SERIALIZZAZIONE DESERIALIZZAZIONE
Per serializzazione si intende un procedimento attraverso il
quale dati di qualsiasi tipo presenti in memoria vengono
rappresentati in una sequenza di byte che può essere poi
salvata in un file per poter essere recuperata successivamente
(con l'operazione inversa, detta deserializzazione)

Questa operazione viene eseguita con la libreria pickle


!!!!!!!! Nota sulla sicurezza: Quando si caricano i dati memorizzati in un pickle, si deve tenere
presente che in esso potrebbero essere memorizzate anche funzioni da richiamare. Ciò comporta un rischio: mai caricare dati da un pickle
di fonte non fidata

Di conseguenza conviene serializzare un oggetto senza metodi


struct

Per poter scrivere dati in un file binario è necessario trasformarli in sequenze
di byte con esplicitazione del modo in cui queste sequenze sono
rappresentate (ad esempio, quanti byte per un numero intero, se il numero è
con o senza segno, se l'ordine dei byte è big-endian o little-endian, ecc.)






DATABASE


Uno strato unico di accesso ai dati, composto da un insieme di funzioni standard

Step per utilizzare i DATABASE


• L'importazione del modulo API.
• Acquisire una connessione con il database.
• L'emissione di istruzioni SQL e stored procedure.
• Chiusura della connessione
• Python ha un supporto integrato SQLite
• Vediamo i concetti utilizzando MySQL non ha un'interfaccia con Python 3, quindi si farà uso del modulo PyMySQL v2.0.

'''

miofile = open('html.txt','w',encoding='utf8') # apre il file in scrittura
miofile.write('riga 1\n') # scrive riga 1
miofile.write('riga 2\n') # scrive riga 2
miofile.write('riga 3\n') # scrive riga 3
miofile.close() # chiude il file
miofile = open('html.txt','r') # apre il file in lettura
print( miofile.readlines())
#print ('stampa doc string :'+miofile.__doc__)
print (miofile)

#
#   SERIALIZZAZIONE DESERIALIZZAZIONE
#
import pickle
data=('foo', 'bar', 'baz')
f = open('mydata', 'wb')
pickle.dump(data, f, pickle.HIGHEST_PROTOCOL) # utilizzo un protocollo di alto livello
f.close()
data=()
f = open('mydata', 'rb')
data = pickle.load(f)
f.close()
print(data)

#
#   SERIALIZZAZIONE di una classse
#


class Foo():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Foo «%s»' % self.name

data = (
        Foo('abc'), Foo('def'), Foo('ghi'),
        ['uno', 'due', 'tre'],
        {'a': 'primo', 'b': 'secondo', 'c': 'terzo'}
    )
with open('mydata1', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
f.close()

#
#    DESERIALIZZAZIONE DI UNA CLASSE
#

data=()
f = open('mydata1', 'rb')
data = pickle.load(f)
f.close()
print(data)
print(data[0])

#
#   struct
#

import struct
FORMAT='<2hf'


'''
Valori della formattazione 
1. '<': che l'ordine dei byte è little-endian
2. 'h': che segue un intero corto di due byte
3. 'f': che segue un numero in virgola mobile di quattro byte

'''

data = struct.pack(FORMAT, 30000, -12, 2.35) #packing
items = struct.unpack(FORMAT, data) #unpacking
print(items)



name="Antonio Giovanni Lezzi"
age=35
FORMAT='<20sb'
data = struct.pack(FORMAT, name.encode('UTF-8'), age)
#packing
items = struct.unpack(FORMAT, data) #unpacking
print(items[0].decode('UTF-8'), items[1])

'''

Si noti che in questo caso la stringa viene codificata in formato UTF-8 e
poi messa in una stringa di 20 caratteri (per cui il valore viene
troncato).

'''


class Person():
    struct_format = struct.Struct('<20sb')
    def __init__(self, name, age):
        self.name = name.strip('\0x00 ')
        self.age = age
    def getPacked(self):
        return self.struct_format.pack(self.name.encode('UTF-8'),self.age)
    def __str__(self):
        return 'Nome: %s, età: %d' % (self.name, self.age)

people = (Person('Mario Rossi', 20),
Person('Giuseppe Verdi', 21),
Person('Roberto Grigio', 22),
Person('Elena Gialli', 23))
with open('people.dat', 'wb') as f:
    for person in people:
        f.write(person.getPacked())

with open('people.dat', 'rb') as f:
    while True:
        data = f.read(Person.struct_format.size)
        if not data:
            break
        name, age = Person.struct_format.unpack(data)
        p = Person(name.decode('UTF-8'), age)
        print(p)


#
#   ________________ DATABASE __________________________________________
#
'''

Scaricare il file zip dal seguente riferimento e decomprimerlo eseguendo i seguenti passi:
• https://github.com/PyMySQL/PyMySQL
cd PyMySQL*
python setup.py install
• Si devono avere i privilegi di Amministrazione e PyPy installato

Oppure è possibile scompattare la libreria nella nostra cartella del progetto, LA DIRECTORY PER MYSQL è PyMySQL


• Le transazioni sono un meccanismo che assicurano la consistenza dei dati, queste hanno le seguenti proprietà:
• Atomicity: Una transazione non deve esser interrotta da altre transazioni ma deve esser disturbata da ciò che può
capitare
• Consistency: una transazione deve cominciare in uno stato consistente e lasciare il sistema consistente
• Isolation: I risultati intermedi di una transazione non sono visibili al di fuori delle transazione corrente
• Durability: una volta che la transazione è stata consegnata, i dati sono persistenti anche dopo un problema fisico di
sistema



sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()


• COMMIT: è una operazione il quale fornisce al DBMS il segnale di finalizzare i cambiamenti,
        dopo questa operazione nessun cambiamento può esser ripristinato, si effettua questa
        operazione invocando il metodo commit()
        db.commit()
• ROLLBACK: nel caso in cui non si sia soddisfatti di uno o più cambiamenti e si vuole
        ripristinare lo stato iniziale allora si usa il metodo rollback()
        db.rollback()
• Disconnessione: Per chiudere la connessione di un DB si usa il metodo close()
                  db.close()


DATABASE ERRORI

L'API DB definisce una serie di errori che devono esistere in ogni modulo del database fornite nella tabella seguente


DATABASE: ERRORI
Eccezione                           Descrizione
Warning             Utilizzato per le questioni non fatali
Error               Classe base per gli errori
InterfaceError      Utilizzato per errori nel modulo di database, non il database stesso
DatabaseError       Utilizzato per gli errori nel database
DataError           Sottoclasse di DatabaseError che si riferisce a errori nei dati.
OperationalError    Sottoclasse di DatabaseError che si riferisce a errori come la perdita di una connessione al
                    database. Questi errori sono generalmente al di fuori del controllo del scripter Python.
IntegrityError      Sottoclasse di DatabaseError per le situazioni che potrebbero danneggiare l'integrità
                    relazionale, come i vincoli di unicità o chiavi esterne.
InternalError       Sottoclasse di DatabaseError che si riferisce ad errori interni al modulo database, ad
                    esempio un cursore non attivi.
ProgrammingError    Sottoclasse di DatabaseError che si riferisce a errori come un nome di tabella errato e
                    altre cose che possono tranquillamente essere attribuiti ad un errore dello sviluppatore.
NotSupportedError   Sottoclasse di DatabaseError che si riferisce al tentativo di chiamare la funzionalità non
                    supportata.


ESEMPIO :

import PyMySQL
# Apertura di una connessine al DB
db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )
# creazione di un cursor
cursor = db.cursor()
# esecuzione della query SQL usando il metodo execute()
cursor.execute("SELECT VERSION()")
# Ottiene un singolo record usando il metodo fetchone()
data = cursor.fetchone()
print("Database version : %s " % data)
# chiusura connessione dal server
db.close()





import PyMySQL
db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Giuseppe', 'Verdi', 40, 'M', 2000)
try:
cursor.execute(sql)
db.commit()
except:
db.rollback()
db.close()



con.execute('insert into Login values("%s", "%s")' % (user_id, password))

______________________ con il triplo " posso scrivere su multiriga
sql = """CREATE TABLE EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""
___________________________ inserimento con una tupla
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%c', '%d' )" % ('Giuseppe', 'Verdi', 40, 'M', 2000)

______________ inserimento con variabili
con.execute('insert into Login values("%s", "%s")' % \
            (user_id, password))



fetchone() per ottenere un record singolo 
fetchall() per ottenere tutte le righe

• fetchone(): il metodo restituisce la prossima riga dei dati in base all’interrogazione effettuata
                sulla base dei dati disponibili e sui risultati ottenuti. Un result set è un oggetto ottenuto quando un
                cursore viene usato per interrogare una tabella
• fetchall(): restituisce tutte le colonne in un resultset, se alcune righe sono state già estratte
            allora una ulteriore invocazione del metodo restituisce le righe rimanenti dal resultset
• rowcount: è un attributo di sola lettura e restituisce il numero di record che sono stati generati
            dall’esecuzione del metodo execute()


import PyMySQL
db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
sql = "SELECT * FROM EMPLOYEE \
        WHERE INCOME > '%d'" % (1000)
try:
    cursor.execute(sql)
    results = cursor.fetchall() # Fetch tutti i dati in una lista di liste
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # stampa dei dati
        print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
        (fname, lname, age, sex, income ))
except:
    print ("Error: unable to fecth data")
db.close()


'''
