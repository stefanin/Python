'''
Sistema di ticketing 
diversi Spettacoli
min 3 max 5 Ticket
c'è un Bottegnino
la Mascherina controlla l'acceso e da il via allo spettacolo
simulare nel Main le istanze degli oggetti in loco con acquisti di diversi spettacoli
'''

#Ticket

class Ticket:
    stato="Valido"
    NomeSpettacolo=""
    def __init__(self, Spettacolo):
        self.NomeSpettacolo=Spettacolo.Nome
    def convalida(self):
        self.stato="Strappato"
    def nullo(self):
        self.stato="Nullo"
    def __str__(self):
        return str(self.stato)

#Spettacolo

class Spettacolo:
    Nome=""
    Partecipanti_min=0
    Partecipanti_max=0
    nTicket=[]
    def __init__(self,Nome,Partecipanti_min,Partecipanti_max):
        '''idSpettacolo,Nome,Partecipanti_min,Partecipanti_max'''
        self.Nome=Nome
        self.Partecipanti_min=Partecipanti_min
        self.Partecipanti_max=Partecipanti_max

    def __str__(self):
        #return "Nome Spettacolo :",str(self.Nome), " Partecipanti : ",str(self.Partecipanti)," Capienza sala : ",str(self.Partecipanti_max)  con le virgole restituisce una TUPLA !!!!!!!
        return "Nome Spettacolo :"+str(self.Nome)+" Partecipanti : "+str(len(self.nTicket))+" Capienza sala : "+str(self.Partecipanti_max)
    
    def addTicket(self,Ticket):
        self.nTicket.append(Ticket)
    
    def verifica(self):
        if len(self.nTicket) <= self.Partecipanti_max:
            return True
        else:
            return False





    


#Botteghino
class Botteghino:
    
    def vendeTicket(self,Spettacolo):
        TK=Ticket(Spettacolo)
        if Spettacolo.verifica():
            Spettacolo.addTicket(TK)
            return TK
        else:
            TK.nullo()
            return TK
            

#Mascherina

        
SP1=Spettacolo("primo Spettacolo",3,5)
SP2=Spettacolo("secondo Spettacolo",3,5)
Bott=Botteghino()
print(SP1)
print(SP2)
print("vendo primo biglietto SP1")
tk1=Bott.vendeTicket(SP1)
print(tk1)
print(SP1)