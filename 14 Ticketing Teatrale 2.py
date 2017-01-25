import random 


#Ticket

class Ticket:
    __stato="Valido"
    __idTicket=0
    def __init__(self):
        self.__idTicket=random.randrange(1,1111111111)
    def convalida(self):
        self.__stato="Strappato"
    def nullo(self):
        self.stato="Nullo"
    def __str__(self):
        return self.__stato+" "+str(self.__idTicket)
    @property
    def stato(self):
        return self.__stato
    @property
    def NomeSpettacolo(self):
        return self.__NomeSpettacolo

#a=Ticket("spettacolo A")


class Spettacolo:
    __Nome=""
    __Partecipanti_min=0
    __Partecipanti_max=0
    __Ticket=[]
    __NumeroTicket=0
    def __init__(self,Nome,Partecipanti_min,Partecipanti_max):
        '''idSpettacolo,Nome,Partecipanti_min,Partecipanti_max'''
        self.__Nome=Nome
        self.__Partecipanti_min=Partecipanti_min
        self.__Partecipanti_max=Partecipanti_max
    def __str__(self):
        return "Nome Spettacolo :"+str(self.__Nome)+" | Capienza sala : "+str(self.__Partecipanti_max) + " | Occupazione Sala : "+str(self.__NumeroTicket)

    @property
    def NomeSpettacolo(self):
        return self.NomeSpettacolo

    def addTicket(self):
        if self.__NumeroTicket < self.__Partecipanti_max:
            tk1=Ticket()
            self.__Ticket.append(tk1)
            self.__NumeroTicket+=1
    def ListaTicket(self):
        for T in self.__Ticket:
            print(T)
    


#Teatro (DB)

class Teatro:
    __nome=''
    __nSpettacolo={}
    # addSpettacolo
    def addSpettacolo(self, Sala,NomeSpettacolo,minInsala,maxInSala):
        sp1=Spettacolo(NomeSpettacolo,minInsala,maxInSala)
        self.__nSpettacolo[Sala]=sp1
    def List(self):
        print(self.__nSpettacolo.items())
    def nSale(self):
        print(len(self.__nSpettacolo.keys()))
    # 
    # listSpettacolo    
    def ListSpettacolo(self):
        for L in self.__nSpettacolo:
            #print("Sala : "+str(L)+" | "+self.__nSpettacolo[L])
            print(str(L)+"° Sala ",end="")
            print(self.__nSpettacolo[L])
    # addTicket
    def addTicket(self,Sala):        
        self.__nSpettacolo[Sala].addTicket()
    # listTicket
    def ListTicket(self,Sala):
        self.__nSpettacolo[Sala].ListaTicket()
            

T=Teatro()
T.addSpettacolo(0,"babau",3,5)
T.addSpettacolo(1,"micio micio",3,5)
T.ListSpettacolo()
print("Primo ticket sala 0")
T.addTicket(0)
print("Primo ticket sala 1")
T.addTicket(1)


T.ListTicket(0)
T.ListTicket(1)