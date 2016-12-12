#media matematica passandogli una lista o tupla

def mediadivalori(*valori): #gli paso i valori di una tupla/lista
    somma=0
    for i in range(0,len(valori)):
        somma+=valori[i]
    return somma/len(valori)

V=[1,1,10,1]

print(str(mediadivalori(1,1,10,1)))


def mediadivalori1(valori): # gli passo la tupla/lista
    somma=0
    for i in range(0,len(valori)):
        somma+=valori[i]
    return somma/len(valori)


TUP=(1,4,5,10)
print(str(mediadivalori1(TUP)))
