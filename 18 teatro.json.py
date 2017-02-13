import http.client
import json

conn = http.client.HTTPConnection("letus.vfdns.org", 80)
conn.request("GET", "/java/teatro/teatro.json")
res = conn.getresponse()
jsonStr = str(res.read().decode("utf-8"))
data = json.loads(jsonStr)
conn.close()
print(data)
print()
print("Elenco")
for a in data:
    if a == "postidisponibili":
        print("Posti Disponibili : ")
        posti=data[a]
        for b in posti:
            print("                      "+b+" : "+str(posti[b]))
    else:        
        print(a+" : "+str(data[a]))
#
#
# mw.php?id=1
#
#
print("")
print(" HTTP GET            :")
conn = http.client.HTTPConnection("sclab.altervista.org", 80)
conn.request("GET", "/mag/mw.php?id=1")
res = conn.getresponse()
print(res.read().decode("utf-8"))

# https://github.com/stefanin/Python



HOSTNAME = 'github.com'

conn = http.client.HTTPSConnection(
	HOSTNAME
)
conn.putrequest('GET', '/stefanin/Python')
conn.endheaders()
response = conn.getresponse()
print (response.read())



