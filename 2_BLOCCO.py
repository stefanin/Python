<<<<<<< HEAD
#commento a linea singoal
'''
commento su linea multipla, utilizzo sconsigliato
'''

'''
BLOCCO:
 istruzione1
 isttuzione2
fine blocco 

VARIABILE

nome_vriabile = valore dichiarare sempre le variabili

'''
a="viva python"
b=3
c, d = "insegnato", "a scuola"# ssegnamento multiplo dividendo il valore con una , 'virgola'
print(a,b,c,d,"\n")
print(9/2)
print(int(10.6)) #converte in int
print(float(20))
print(int(10.6),float(20))
print(int(10.6),float(20),sep='')

a=1
b="2"
print(a+int(b))#somma una un intero e una stringa trasformandola in int

#STRINGHE
print('a'+'b') #concatenamento
print("a"*5)#ripetizione

s="Ciao mondo"
print(s[0])#indicizzazione
print(len(s))#lunghezza
print(s[2:7]) #operatore di slising. prende il carattere da posizione 2 a 7
print(s[4:]) #operatore di slising. prende i caratteri fino posizione 4
print(s[:4]) #operatore di slising. prende i caratteri da posizione 4
print(s.find('mon')) #posizione stringa
print(s.replace("mondo","pirloni"))#sostituisce la stringa
print(s.upper())#UPPERCASE

risultato="aaaa"+"bbbb"
print(risultato)
print("'%s' e '%d'"% ("stringa", 7))
nome="stefano"
anni=46
print("%s ha %d" % (nome,anni)) # operatore % è un segnaposto %s = parametro striga, %d = parametro numerico

#________________________________ metodo input ______________________
valore=eval(input("inserisci il valore numerico "))
print("valore :",valore)
print(valore*valore)
print("oppure ")
valore2=int(input("inserisci quello che vuoi "))
print("eccolo",valore2)

#__________________________ esercizio
nome="stefano cornelli"
print("\n"+nome[6:]+nome[:7])

print("operazioni matematiche")
print("1+1 ",1+1)
print("1-1 ",1-1)
print("1*1 ",1*1)
print("1/1 ",1/1)
print("modulo 25/7 ",25%7) #modulo
print("arrotonda 8.3/3 ",8.3//3,"divide",8.3/3) #operatore arrotondamento
print("potenza",8**2)

print("1/1 ",0/1)
a="0"
b="1000"
print(a+b)
print(int(a)+int(b))
a=5
a+=6
print(a)
x="Ciao"
print("C" in x) #operatore membership o operatore di appartenenza
print("C" not in x) #operatore membership o operatore di appartenenza
print("C" is x) #operatore se uguale tipo e contenuto
print("C" is not x) #operatore se uguale tipo e contenuto

#
#       in operatore di appartenenza !!!!
#
#       is operatore uguale !!



#_______________________________________esercizio
v="elimino lo spazio"
print(v.replace(" ",""))





=======
#commento a linea singoal
'''
commento su linea multipla, utilizzo sconsigliato
'''

'''
BLOCCO:
 istruzione1
 isttuzione2
fine blocco 

VARIABILE

nome_vriabile = valore

'''
a="viva python"
b=3
c, d = "insegnato", "a scuola"# ssegnamento multiplo dividendo il valore con una , 'virgola'
print(a,b,c,d,"\n")
print(9/2)
print(int(10.6)) #converte in int
print(float(20))
print(int(10.6),float(20))
print(int(10.6),float(20),sep='')

a=1
b="2"
print(a+int(b))#somma una un intero e una stringa trasformandola in int

#STRINGHE
print('a'+'b') #concatenamento
print("a"*5)#ripetizione

s="Ciao mondo"
print(s[0])#indicizzazione
print(len(s))#lunghezza
print(s[2:7]) #operatore di slising. prende il carattere da posizione 2 a 7
print(s[4:]) #operatore di slising. prende i caratteri fino posizione 4
print(s[:4]) #operatore di slising. prende i caratteri da posizione 4
print(s.find('mon')) #posizione stringa
print(s.replace("mondo","pirloni"))#sostituisce la stringa
print(s.upper())#UPPERCASE

risultato="aaaa"+"bbbb"
print(risultato)
print("'%s' e '%d'"% ("stringa", 7))
nome="stefano"
anni=46
print("%s ha %d" % (nome,anni)) # operatore % è un segnaposto %s = parametro striga, %d = parametro numerico

#________________________________ metodo input ______________________
valore=eval(input("inserisci il valore numerico "))
print("valore :",valore)
print(valore*valore)
print("oppure ")
valore2=int(input("inserisci quello che vuoi "))
print("eccolo",valore2)

#__________________________ esercizio
nome="stefano cornelli"
print("\n"+nome[6:]+nome[:7])

print("operazioni matematiche")
print("1+1 ",1+1)
print("1-1 ",1-1)
print("1*1 ",1*1)
print("1/1 ",1/1)
print("modulo 25/7 ",25%7) #modulo
print("arrotonda 8.3/3 ",8.3//3,"divide",8.3/3) #operatore arrotondamento
print("potenza",8**2)

print("1/1 ",0/1)
a="0"
b="1000"
print(a+b)
print(int(a)+int(b))
a=5
a+=6
print(a)
x="Ciao"
print("C" in x) #operatore membership
print("C" not in x) #operatore membership
print("C" is x) #operatore se uguale tipo e contenuto
print("C" is not x) #operatore se uguale tipo e contenuto

#_______________________________________esercizio
v="elimino lo spazio"
print(v.replace(" ",""))





>>>>>>> a77d11ac17b8a83d3be708f5d88bab1c59680f21
