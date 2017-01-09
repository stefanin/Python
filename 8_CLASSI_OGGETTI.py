'''
L'oggetto è un entità con all'interno dei contenuti, esso li può rendere pubbici o privati attraverso 
delle funzioni. La classe è il modello per definire l'oggetto
Le variabili contenute nell’oggetto, che si chiamano dati membri
Le funzioni contenute nell’oggetto, che si chiamano metodi

Le informazioni poso essere :

Pubblico
Protetto

class <nome classe> [(<classe madre>,…)]:
    <elenco dati membro da inizializzare>
    <elenco metodi>


Ogni metodo deve avere come primo parametro l’oggetto stesso, si utilza il
parametro

self 

'''
class Corsi:
    titolo=""
    descrizione=""
    def stampa(self):
        print(self.titolo,self.descrizione)


class persona:
    nome = ""
    cognome = ""
    indirizzo = ""
    __telefono = "" #Per indicare di tenere protetti i dati membri e quindi realizzare veramente l’incapsulamento, si deve anteporre al nome della variabile i caratteri “__” ( 2 underscore)
    stato_civile = ""
    corso = Corsi()

    def __init__(self,n,c,i=""):# COSTRUTTORE  __init__ metodo standard per inizializzare l'oggetto
        self.nome=n
        self.cognome=c
        self.indirizzo =i
    def cambia_indirizzo(self,s): # uyilizzo self per poter assegnare la variabile
        self.indirizzo = s
    def cambia_telefono(self,s):
        self.telefono = s
    def cambia_stato_civile(self,s):
        self.stato_civile = s
    def stampa(self):
        print(self.nome,self.cognome,self.indirizzo,self.stato_civile,self.__telefono)
        self.corso.stampa()


'''
per definire una funzione bisogna passare il paramento self :

def aaaa(self):
    
def aaaa(self, variabile)

Può essere una buona pratica dichiarare gli attributi in
modalità privata e racchiudere il codice da usare per
assegnare un valore ad uno degli attributi in una
funzione speciale, in modo da poter fare tutti i controlli
che desideriamo

ATTENZIONE, la variabile viene creata al momento in cui viene usata, qundi se in una classe 
creiamo :

a =persona('stefano','cornelli')
a.ziofelice="aaaaaa"
print(a.ziofelice)

la variabile ziofelice non esiste nell'oggetto ma è possibile usarla

se era presente una variabile 'ziofelice' all' interno dell'oggetto, python utilizza quest'ultima.
Ma se la variabile è protetta python utilizza la variabile esterna !!!!!


__dict__ : dizzionario che contiene tuttte le variabili dell'oggetto, quindi :
    print(oggetto.__dict_) stampa tutte le variabili


Metodo di classe state less :

vengono utilizzati per risparmiare codice

class Picture():
    def doSomething(self, n):
    print("Devo fare qualcosa con il valore %d." % n)

    def codice(nome,cognome)        <----------- metodo statico
        print(nome,cognome)

img1=Picture()
img1.doSomething(42) # uso il nome dell’istanza


Picture.doSomething(img1, 42) # uso stateless il nome della classe e passo l'istanza come primo parametro
Picture.codice("AAAA","BBBBB")


'''


a =persona('stefano','cornelli')
a.corso.descrizione="imparare python"
a.corso.titolo="Python"
a.indirizzo="via sandro pertini"
a.stampa()

a.__telefono = "334" #essendo una variabile protetta non viene assegnata
a.stampa()
a.ziofelice="aaaaaa"
print(a.ziofelice)


'''
def setWidth(self, value):
    assert(isinstance(value, int))
    assert(value>=0)
    self.__width = value
    return self
def setHeight(self, value):
    assert(isinstance(value, int))
    assert(value>=0)
    self.__height = value
    return self

img1.setWidth(2000).setHeight(3000)


se il metodo ritorna lo stesso oggetto, con una riga di cosice puoi accodare più metodi

'''