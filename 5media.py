#media matematica passandogli una lista o tupla

def mediadivalori(valori):
    somma=0
    for i in range(0,len(valori)):
        somma+=valori[i]
    return somma/len(valori)

V=[1,1,10,1]

print(str(mediadivalori(V)))

TUP=(1,4,5,10)
print(str(mediadivalori(TUP)))
