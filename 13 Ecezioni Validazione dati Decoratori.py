'''
Ecezioni

Errori sintattici e Errori di runtime che non possiamo prevedere



a,b = 5, 0
print(a/b)

    print(a/b)
ZeroDivisionError: division by zero


try:
<gruppo di istruzioni sotto test>
except:
<gruppo di istruzioni da eseguire in caso di errore>
else: # opzionale viene eseguito se funziona try
<gruppo di istruzioni2>
finally: # opzionale, al posto di except e viene usato come terminarore di tutte le ecezzioni
<gruppo di istruzioni3>



'''
a,b = 5, 0
try:
 print(a / b)
except:
 print("non hai studiato matematica!")


print ("divisione 0")
try:
    print("operazione 1")
    print("operazione 2")
    print(a / b)
    print("operazione 3")
    
except:
    print("non hai studiato matematica, ma con python sei forte!")
else:
    print("sei nel else:")

finally:
    print("sei nel finally:")
    
print ("\n\n divisione 1")
try:
    print("operazione 1")
    print("operazione 2")
    print(a / 1)
    print("operazione 3")
    
except:
    print("non hai studiato matematica, ma con python sei forte!")
else:
    print("sei nel else:")

finally:
    print("sei nel finally:")



print ("\n\n divisione 0 con ZeroDivisionError")
try:
    print("operazione 1")
    print("operazione 2")
    print(a / 0)
    print("operazione 3")
    
except ZeroDivisionError as z:
    print("non hai studiato matematica, ma con python sei forte! e usi ZeroDivisionError la b=",z)

except:
    print("non hai studiato matematica, ma con python sei forte! e non ho capito che cosa è andato storto")
    

else:
    print("sei nel else:")

finally:
    print("sei nel finally:")


print ("\n\n divisione 0 con ZeroDivisionError")

b=0
try:
    print("operazione 1")
    print("operazione 2")
    if b==0:
        raise Exception
    print(a / b)
    print("operazione 3")
    
except ZeroDivisionError:
    print("non hai studiato matematica, ma con python sei forte! e usi ZeroDivisionError")

except:
    print("non hai studiato matematica, ma con python sei forte! genero l'ecezzione controllando se b=0")
    

else:
    print("sei nel else:")

finally:
    print("sei nel finally:")
    
print()


def checked_input(message, constraint_class):
    """Permette l'inserimento di un valore in maniera controllata.
Chiede in input una stringa usando *message* come prompt, poi
tenta la conversione nella classe *constraint_class* e
restituisce il valore convertito.
Se viene inserito un valore non valido, viene richiesto di
nuovo l'inserimento.
"""
    while(True):
        v=input(message)
        try:
            n = constraint_class(v)
            return n
        except ValueError as err:
             print("Sembra che tu non abbia inserito un valore valido…", err)

#print(checked_input("inserisci un intero",int))

'''

Decoratore

Un decoratore è una normale funzione che modifica un'altra funzione, può essere usato per modificare la funzione senza toccare il codice originale
la sequenza di utilizzo è la seguente :


DEFINIRE IL DECORATORE
@ASSEGNO IL DECORATORE
FUNZIONE 


Alcuni esempi di decoratori sono @staticmethod, @property ecc




PROPRIETA'


class Fruit(object):
    .....
    @property
    def quality(self):
        return self.__quality
    
    @quality.setter      ...... .setter è mandatory per assegnare il decoratore 
    def quality(self, value):
        if 0 <= value <= 100:
            self.__quality = value
        else:
            self.__quality = 50
            self.__addAlert('bad quality: %d' % value)


myapple = Fruit('mela granny smith') .....  creo l'oggetto
myapple.quality = 10   ................... assegno un valore e utilizzo il decoratore quality.setter             
print('quality %d' % myapple.quality) .... uso il decoratore property



    @property
    def is_good(self):
        return self.quality > 70

myapple.quality= 30
print(myapple.quality, myapple.is_good)  Alcune proprietà possono essere calcolate a partire dal valore degli attributi. Per esse si può impostare solo il getter, e non il setter

'''


# creiamo un decoratore
def mio_decoratore(funzione_da_decorare):
    #fai qualcosa con la funzione, per es.
    funzione_da_decorare.prova = "prova"
    return funzione_da_decorare

#definiamo una funzione
@mio_decoratore
def molt(a, b):
    return a * b

molt = mio_decoratore(molt)
print ("stampo molt senza decoratote", molt)
print ("stampo molt con decoratore", molt.prova)



def mio_decoratore(funzione_da_decorare): # creo il decoratore
    def wrapper():
        print("Sono dentro la funzione wrapper e posso accedere alla funzione %s" % funzione_da_decorare.__name__)
        return funzione_da_decorare()
    return wrapper

@mio_decoratore  # uso il decoratore
def foo():
    print("Io sono la funzione da decorare")

foo()



def mio_decoratore(funzione_da_decorare):
    def wrapper(*args, **kwargs):    #.................. *args trasforma in lista 1,2 e **kwargs trasforma foo="foo" in dizionario
        #Con gli argomenti possiamo fare ciò che vogliamo
        kwargs['foo'] = "argomento modificato"
        print("Stiamo chiamando la funzione %s con argomenti %s e parole chiave %s" % (funzione_da_decorare.__name__, args,kwargs))
        return funzione_da_decorare(*args, **kwargs)
    return wrapper

@mio_decoratore

def molt(a, b, foo = "foo"):
    print(foo)
    return a * b


print(molt(1, 2))



class Fruit(object):
    __quality=0
    __descrizione=""

    def __init__(self, descrizione):
        self.__descrizione=descrizione

    @property
    def quality(self):
        return self.__quality
    
    @quality.setter      
    def quality(self, value):
        if 0 <= value <= 100:
            self.__quality = value
        else:
            self.__quality = 50
            #self.__addAlert('bad quality: %d' % value)




a = Fruit("prova")
a.quality=10
print(a.quality)
a.quality=102
print(a.quality)