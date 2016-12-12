def palindroma(parola):
    #confronta la stringa inversa [::-1]
    if (parola==parola[::-1]): 
        return True 
    else: 
     return False
def palindroma2(parola):
    #confronta la stringa inversa [::-1]
    if (parola==parola[::-1]): 
        return True 
    return False # in questo caso evito il costrutto else !!!

def palindroma3(parola):
    #confronta la stringa inversa [::-1]
    if (parola==reversed(parola)): 
        return True 
    return False # in questo caso evito il costrutto else !!!


if (palindroma(input("Inserisci una parola :"))): 
    print("è palindroma ") 
else: 
    print("non è palindroma") 

if (palindroma3(input("Inserisci una parola :"))): 
    print("è palindroma ") 
else: 
    print("non è palindroma") 
