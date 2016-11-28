
#_______________ ciclo for con range
for count in range(1,10):
 print (count)



'''
        Funzioni

sono un strumento per strutturare il codice creando un blocco 

si definiscono come segue :


def nome_funzione(parametro1, parametro2, ..):
    corpo della funzione
    xxxx
    xxxxx
    xxxx
    return <risultatao> (optional, il valore di defult è nullo)

E' possible definire dei valori predefiniti dei paramentri ..(aaa=7)

la parola PASS permette di parcheggiare una funzione 


Per passare più paramentri bisogna utilizzare *

def funzione(*parametro):
    for parametro in tantiparametri:
     print(tantiparametri)

def funzione()
    PASS


'''
def stampa(scritta,ritorno="nessuno"):
    print(scritta,end='')
    return ritorno
stampa("la variabile scritta","")
print()
print(stampa("stampa la variabile scritta e il valore di ritorno ","torno"))
print(stampa("il valore predefinito è "))


def passatutto(*passa):
    for ssll in passa:
     print(ssll)

passatutto("aaaa","bbbb","ccc")


'''

                LISTE

sequenza all'interno di parentesi quadre [] 

Lista Vuota 

a=[]

lista di numeri 

nome_lista = [1,4,5,6,7]

lista mista

nome_lista = [1,4,"5",6,7]

lista annidata

nome_lista = [1,4,"5",[3,4,5,"7"],7]

range(1,8) funzione nativa che genera una lista di numeri
'''
nome_lista = ["1","7","5"]
print(nome_lista[2])
nome_lista[2]="babau"
print(nome_lista[2])

#assegno una sotto lista
nome_lista[2]="[1,2,3]"
print(nome_lista[2][1])

# modifico con lo slicing
nome_lista[1:3]=["a","b","c"]
print(nome_lista[2])

#inserimento in coda
nome_lista.append("inserito alla fine")
for a in nome_lista:
    print(a)

# operatore +

nome_lista.insert(0,"primo")
print(nome_lista[0])
del nome_lista[0] # rimuove l'oggetto all' indice 0
print(nome_lista[0])

nome_lista.remove("a") # rimuove l'oggetto
del nome_lista[0:3]
print(nome_lista[0])

nome_lista.clear()
# canclella tutta la lista e di fatto print(nome_lista[0]) va in errore


def funzione_fuffa():
    pass


#funzione che chiede il numero di tentativi per indovinare la passowr utilizzando le funzioni


def verifica_passowrd(num_tentativi=3,password="babau"):
    conta=1
    while conta <=num_tentativi:
        insPassword=input("Inserisci la passowrd, tentativo numero "+str(conta)+" : ")
        if insPassword == "babau":
            return True
        else:
            print("passowrd toppata !!!")
        conta +=1

if verifica_passowrd(int(input("quanti tentativi vuoi fare ")):
    print("bravo")
else:
    print("riprova domani testina")