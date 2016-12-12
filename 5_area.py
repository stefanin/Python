'''

Riscrivete il programma ‘area.py’, definendo funzioni separate per l’area del quadrato, del rettangolo
e del cerchio (3.14 * raggio**2). Il programma deve includere anche un’interfaccia a menu

'''

def areaQuadrato(lato):
    return lato*lato

def areaRettangolo(altezza,lunghezza):
    return altezza * lunghezza

def areaCerchio(raggio):
    return 3.14 * raggio**2

def acapo(n):
    i=1
    while i <= n:
        print()
        i+=1

#menu
while True:
    print("scegli quale operazione vuoi fare :")
    acapo(2)
    print("1 . per area Quadrato")
    print("2 . per area Rettangolo")
    print("3 . per area Cerchio")
    print("0 . per uscire")
    scelta=input()
    
    valori_accettati=('0','1','2','3')
    for valori in valori_accettati:
        if scelta==valori:
            acapo(2)
            if scelta=='0':
                exit()
            elif scelta=='1':
                l=int(input("valore lato : "))
                print(areaQuadrato(l))
            elif scelta=='2':
                altezza=int(input("altezza : "))
                lunghezza=int(input("lunghezza : "))
                print(areaRettangolo(altezza,lunghezza))
            elif scelta=='3':
                raggio=int(input("raggio : "))
                print(areaCerchio(raggio))
            else :
                print("tasto sbagliato ...")

