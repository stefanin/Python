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

print()         #print() stampa un \n

val=10
while val < 20:
 print(str(val)+" ",end="")
 val+=2
 if val==16:
  break
print()
conta=0
while True:                     # ciclo infinito
 print(str(conta)+" ",end="")
 conta+=1
 if conta == 50:
  break

# if/els nel ciclo while e for


 # CICLI con brack permette di uscire dal ciclo

print()
for val in "python":
 if val == "h":
  break
 print(val)


 # CICLI con continue permette di saltare alla prima istruzione del ciclo
print()
for val in "python":
 if val == "h":
  continue
 print(val)

print()
for lettera in 'Ciao.Mondo':
 if lettera == '.':
  pass # non fa nulla
  print("_", end="")
  continue
 print(lettera, end='')

#____________________________ esercizi
'''
Scrivete un programma che chieda all’utente di indovinare una password,
ma che dia al giocatore solamente 3 possibilità, fallite le quali il programma
terminerà, stampando “È troppo complicato per voi”
'''
password="indovinata"
print("indovina la password ha 3 tentativi ....")
tentativo=1
prova=""
while tentativo <= 3 :
 prova=input("Tentativo num. "+str(tentativo)+" :")
 if prova == password:
  print("bravo la passowrd è : "+prova)
  break
 else:
  print("no no no ...")
 tentativo+=1
else:
 print("riprova un altra volta")

'''
Scrivete un programma che chieda due numeri. Se la somma dei due
numeri supera 100, stampate “Numero troppo grande”
'''
print()
num1=0
num2=0
print("inserisci due numeri")
num1=input("primo numero : ")
num2=input("secondo numero : ")
if (int(num1)+int(num2)) > 100:
 print("numero troppo grande")



'''
Scrivete un programma che chieda all’utente il nome. Se viene inserito il
vostro nome, il programma dovrà rispondere con un “Questo è un bel
nome”, se il nome inserito è Mario Rossi o Giuseppe Verdi il programma
dovrà rispondere con una battuta ;) mentre in tutti gli altri casi l’output del
programma sarà un semplice “Tu hai un bel nome!”.
'''
print()
nome=""
nome=input("inserisci il tuo nome e cognome :")
print()
nome=nome.upper()
if nome == "STEFANO CORNELLI":
 print("Questo è un bel nome")
else:
 if (nome == "MARIO ROSSI") or (nome == "MARIO ROSSI") :
  print("hahhhhhhha")
 else:
  print("Tu hai un bel nome")
