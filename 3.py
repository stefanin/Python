#20161121 Condizioni


#  if bloco di codice opzioniali elif e alse seguiti dai :



x=8
z=10
y = int(input("inserisci un numero intero tra 0 e 10: ")) # da stringa il cast lo converte a intero
if y == x:
 print("Il numero inserito è corretto ", y)
elif y > z:
 print("sono consentiti valori compresi tra 0 e "+str(z)+" hai inserito '"+str(y)+"'")
 if (y-x) ==1:
  print("ma ci sei andato vicino")

else:
 print("il numero %s non è corretto" % (y))


 # Ciclo FOR(loop)      consente di ripetere un operazione fino al verificarsi du una condizione

fibonacci = [1,1,2,3,5,8,13,21,34,55,89,144]
for val in fibonacci:
 print(val)
totale=0
for val in fibonacci:
 totale=totale+val
print("il totale è "+str(totale))

# range  definizione di range

for val in range(5,20):
 print(val,end="")
print("\n")
for val in range(5,20,2):
 print(val,end="")

 #          CICLO WHILE 
print("\n")
val=10
while val < 20:
 print(str(val)+" ",end="")
 val+=2
 if val==16:
  break
print("\n")
conta=0
while True:                     # ciclo infinito
 print(str(conta)+" ",end="")
 conta+=1
 if conta == 50:
  break

# if/els nel ciclo while e for