rubrica = []

def ricercaRubricaCon(cognome):
    i = -1
    for item in rubrica:
        if item["cognome"] == cognome:
            i = i + 1
    
    return i

def ricercaRubrica(cognome, nome):
    if len(cognome) <= 0 or len(nome) <= 0:
        print("Nessun dato inserito")
        return None

    for item in rubrica:
        if item["nome"] == nome and item["cognome"] == cognome:
            return item

def inserisciInRubrica(**dizionario):
    rubrica.append(dizionario)

def eliminaDallaRubrica(nome, cognome):
    for item in rubrica:
        if item["nome"] == nome and item["cognome"] == cognome:
            removeItem = item

    if 'removeItem' in globals() and removeItem is not None:
        rubrica.remove(removeItem)
        removeItem = None

def modificaInRubrica(cognome, elemento):
    item = ricercaRubricaCon(cognome)

    if item >= 0:
        rubrica[item] = elemento
        
    else:
        print("Nessun dato da modificare\n")

def visualizzaTuttaRubrica():
    if len(rubrica) == 0:
        print("Rubrica vuota\n")
    else:
        for item in rubrica:
            #print(item)
            print("nominativo:\t" + item["nome"] + " " + item["cognome"] + "\ntelefono:\t" + item["telefono"] + "\nemail:\t" + item["email"] + "\n")
        print("\n")

def menu():
    print("1) ricerca")
    print("2) inserisci")
    print("3) modifica")
    print("4) elimina")
    print("5) visualizza tutta la rubrica")
    print("0) esci")
    print("")

    return int(input("Inserisci scelta: "))

scelta = 9
while scelta != 0:
    scelta = menu()

    if scelta == 1:
        nomeStr = input("Inserisci nome: ")
        cognomeStr = input("Inserisci cognome: ")

        if len(nomeStr) > 0 and len(cognomeStr)> 0:
            print(ricercaRubrica(nomeStr, cognomeStr))
        else:
            print("Nessun dato inserito\n")

    if scelta == 2:
        nomeStr = input("Inserisci nome: ")
        cognomeStr = input("Inserisci cognome: ")
        telefonoStr = input("Inserisci telefono: ")
        emailStr = input("Inserisci email: ")
        inserisciInRubrica(nome=nomeStr, cognome=cognomeStr, telefono=telefonoStr, email=emailStr)

    if scelta == 3:
        nomeRicStr = input("Inserisci nome da ricercare: ") 
        nomeStr = input("Inserisci nome: ")
        cognomeStr = input("Inserisci cognome: ")
        telefonoStr = input("Inserisci telefono: ")
        emailStr = input("Inserisci email: ")

        nuovoItem = dict()
        nuovoItem["nome"] = nomeStr
        nuovoItem["cognome"] = cognomeStr
        nuovoItem["telefono"] = telefonoStr
        nuovoItem["email"] = emailStr

        modificaInRubrica(nomeRicStr, nuovoItem)
    
    if scelta == 4:
        nomeStr = input("Inserisci nome: ")
        cognomeStr = input("Inserisci cognome: ")
        eliminaDallaRubrica(nomeStr, cognomeStr)
    
    if scelta == 5:
        visualizzaTuttaRubrica()


