def palindroma(parola):
    #confronta la stringa inversa [::-1]
    if (parola==parola[::-1]): 
        return True 
    else: 
     return False

if (palindroma(input("Inserisci una parola :"))): 
    print("è palindroma ") 
else: 
    print("non è palindroma") 