#2016/11/30
'''

        TUPLE 

    simile alla lista, non è possibile modificarla e non si posono cancellare

    con * nel paramento di una funzione, la variabile diventa una tupla

'''

#tupla vuota
nome_tupla=()
#tupla con valore
nome_tupla=('Homer')
print(nome_tupla)
#se nella tupla inseriamo una , il compilatore stampa il tipo di data
nome_tupla=('Homer',)
print("questo è il tipo tupla"+str(nome_tupla))
#tupla annidata
nome_tupla=('aa',1,(21,3,7))
print(nome_tupla)
#tupla con una lista
nome_tupla=('aa',1,(21,3,7),[1,5,7])
print(nome_tupla)
#tuple packing
nome_tupla=5,7,9,'aaaa',[1,"ssiii",3]
print(nome_tupla)
#possono essesre indicizzata
print(nome_tupla[4])
#slicing
print(nome_tupla[-3])
#alla fine della tupla
print(nome_tupla[-1])
#tra 0 e 3
print(nome_tupla[0:3])
#escludi i primi 3 elementi
print(nome_tupla[:-3])
#parte dal  3 elemento
print(nome_tupla[3:])
#alla fine della tupla e accedo al 2 elemento
print(nome_tupla[-1][1])
#se nella tupla ho una lista la posso mutare
nome_tupla[-1][1]="nooo"
print(nome_tupla[-1][1])

#possibile riassegnare il valore della tupla

#si possono CONCATENARE
seconda_tupla=('wwww',3.4)
print(nome_tupla+seconda_tupla)
#si possono MOLTIPLICARE
seconda_tupla=('wwww',3.4)
print(nome_tupla*3)

# metodi all() any()

# all() se ci sono tutti i valori restituisce vero TRUE, se in una tupla c'è il valore 0 -> FALSE AND logico
a=(0,4)
print(all(a))

#any() restituisce TRUE se qualsiasi elemento è TRUE o la lista non è vuota OR logico
a=(0,4)
print(any(a))
#False xche è vuota
a=()
print(any(a))
# enumerate() restituisce un oggetto che contiene copie composte

nome_tupla=('aa',1,(21,3,7),[1,5,7])
for i in enumerate(nome_tupla):
    print(i)
print(len(nome_tupla))
# max() e min()
nome_tupla=(1,5,100)
print(str(max(nome_tupla))+" "+str(min(nome_tupla)))
#sorted()
nome_tupla=(1,100,4)
print(sorted(nome_tupla))
#list() trasforma la tupla in una lista
lista = list(nome_tupla)
print(lista)
#tuple() trasforma una lita in tupla


""" 
         in una funzione dopo il : è possibile aggiungere un commento con '''' che viene visto dalle gui 

"""

'''
    FUNZIONE LAMBDA

'''
dividi = lambda dividendo: dividendo /5

print(dividi(10))

def dividi(dividendo):
    return dividendo / 5
print(dividi(10))


"""

        FUNZIONI RICORSIVE

        la funzione può richiamare se stessa

"""


# Utilizzo delle funzioni ricorsive
# per il calcolo del fattoriale di un numero
def fattoriale(n): 
    ''' Il fattoriale di un numero indica il prodotto di quel numero per tutti i suoi antecedenti '''
    if n==1:
        return 1
    else:
        return (n * fattoriale(n-1))
    res = int(input("Inserisci un numero: "))
    if res >= 1:
        print("Il fattoriale di", res, "è", fattoriale(res))

fattoriale(1)



