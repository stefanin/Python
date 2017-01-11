class Lampadina:
    ''' spegni accendi() impostaStato(st) st=True/Folse'''
    stato=False

    def __init__(self,st=False):
        self.stato= st

    def accendi(self):
        self.stato=True

    def spegni(self):
        self.stato=False
    
    def impostaStato(self, st):
        ''' st True o False '''
        self.stato = st
    
    def intettuttore(self):
        self.stato=not(self.stato)
    
    def ottieniStato(self):
        if self.stato:
            return "Accesa"
        else :
            return "Stenta"



def esempioTupla(*args): # passaggio di parametri tipo tupla
    print(args)
    print(type(args))


if __name__ == "__main__":
    l1= Lampadina()
    print("Lanpadina l1 creata con stato",l1.ottieniStato())
    print("Lampadina l1 accesa")
    l1.accendi()
    print("Lanpadina l1 visualizza stato",l1.ottieniStato())
    l1.spegni()
    print("Lanpadina l1 visualizza stato",l1.ottieniStato())
    l1.impostaStato(True)

    print("Lanpadina l1 visualizza stato",l1.ottieniStato())
    l1.intettuttore()
    print("Lanpadina l1 visualizza stato",l1.ottieniStato())
    
    n = int(input("Quante lampadine vuoi ? "))
    scatola=[]
    for i in range(n):
        scatola.append(Lampadina()) # aggiungo alla lista la classe e in automatico creo l'oggetto
    for l in scatola:
        print("lampadina è "+str(l.ottieniStato()))

    scelta = int(input("Quale lampadina vuoi accendere ? "))
    if scelta >=0 and scelta < len(scatola):  #                 oppure 0 <= scelta < len(scatola)
        scatola[scelta].accendi()
    for l in scatola:
        print("lampadina è "+str(l.ottieniStato()))
    

esempioTupla("aaa", 4,False)