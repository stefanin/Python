import http.client
import json

conn = http.client.HTTPConnection("letus.vfdns.org", 80)
conn.request("GET", "/java/teatro/teatro.json")
res = conn.getresponse()
jsonStr = str(res.read().decode("utf-8"))
data = json.loads(jsonStr)
conn.close()
print(data)
print("Elenco")
for a in data:
    print(a+str(data[a]))

