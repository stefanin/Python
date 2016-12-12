#2 è l’unico numero primo pari è 2, 4, 6, 8, o 0, il numero è pari e quindi non è primo.
# Dividi n per ogni numero compreso tra 2 e n-1. Poiché un numero primo non ha fattori oltre a se stesso e 1
# 

def numeroprimo(numero):
    if (numero==1):
        return True
    elif (numero==3):
        return False
    else:
        risultato=True
        for D in range(2,numero-1):
            calcolo=numero/D
            if (calcolo==int(calcolo)):
                risultato=False
                break
        return risultato 
                

if (numeroprimo(int(input("inseriscri numero : ")))):
    print("è un numero primo")
else:
    print("non è un numero primo")
 