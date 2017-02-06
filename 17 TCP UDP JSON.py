'''
RMI = remote machine interface

MIME è un acronimo di "Multipurpose Internet Mail Extensions"


HEADER DI RICHIESTE HTTP
GET /python/images/cup.gif HTTP/1.0
Connection: Keep-Alive
User-Agent: Mozilla/3.01 (Macintosh; I; PPC)
Host: www.oreilly.com:80
Accept: image/gif, image/x-xbitmap, image/jpeg, */*

RISPOSTA DEL SERVER
HTTP/1.0 200 OK
Server: Netscape-Enterprise/2.01
Date: Sat, 02 Aug 1997 07:52:46 GMT
Accept-ranges: bytes
Last-modified: Tue, 29 Jul 1997 15:06:46 GMT
Content-length: 2810
Content-type: text/html

SERVIZI WEB E RICHIESTE REST

• GET: per leggere dati da remoto senza apportare modifiche
• PUT: per richiedere la modifica dei dati pre-esistenti
• POST: per inviare dati verso il servizio con lo scopo di richiederne l’inserimento nella base dati
• DELETE: per cancellare il dato

POST, GET, PUT, DELETE richiamano gli stessi quattro concetti espressi dai metodi CRUD dei database (create, read, update e delete)

POST   = C (informazione nel header dell'http) 
GET    = R (informazioni in chiaro)
PUT    = U
DELETE = D

CODICI DI STATO

• 200: OK
• 400: Bad Request
• 403: Forbidden
• 404: Not found
• 500: Internal Server error

'''

'''from urllib.request import urlopen
for line in urlopen('http://www.python.org/community/diversity/'):
    text = line.decode('utf-8')
    if '<title>' in text:
        print(text)'''


# oppure se ho un webbrowser
import urllib.request
import urllib.parse
import webbrowser
url = 'http://sclab.altervista.org'
#print(webbrowser.open(url)) # Apre un url usando il browser di default

#Ecco un semplice esempio con urllib
#urllib.request.urlretrieve("http://python.org/", "file222.txt")



print("GET")

response = urllib.request.urlopen("http://pyton.org")
html = response.read()
print(html)



url = "http://sclab.altervista.org/mag/mw.php"
values = {'id' : 1 }
data = urllib.parse.urlencode(values)
print(data)
#req = urllib.request.Request(url, data)
response = urllib.request.urlopen(url, data)
#the_page = response.read()





'''





GESTIONE DEL FORMATO
JSON
• Il JSON (Javascript Object Notation) è un formato
stringa per la rappresentazione di dati organizzati
in oggetti e array.



[ <--------------array
    { <--------dizionario
    "nome":"Roberto",
    "eta":52
    },
    {
    "nome":"Antonio",
    "eta":32
    },
    {
    "nome":"Francesca",
    "eta":40
    }
]




import http.client
conn = http.client.HTTPConnection("sclab.altervitsa.org")
conn.request("GET", "/index.php")
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.
conn.request("GET", "/index.php")
r1 = conn.getresponse()
while not r1.closed:
    print(r1.read(200)) # 200 bytes
'''