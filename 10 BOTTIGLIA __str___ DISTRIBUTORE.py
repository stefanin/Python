class bottiglia:
    quantita=0
    contenuto=""
    capacita=0

    def __init__(self,qt,ct):
        self.quantita=qt
        self.contenuto=ct
        self.capacita=qt

    def bevi(self, qt):
        if qt < self.quantita:
            self.quantita -= qt
        else:
            self.quantita=0
    def riempi(self):
        if self.quantita==0:
            self.quantita=self.capacita

    def __str__(self): #    ridefinisco il metodo __str__        
        return "tipo " + self.contenuto + " " + str(self.quantita) + " "+ str(self.capacita)

class distributore:
    l=[]

    def __init__(self, *d):
        self.l= list(d)
    
    def __str__(self):
        descr=""
        for item in self.l:
            descr= descr+ " " + str(item) + "\n"
        return descr




if __name__ == "__main__":
    b1 = bottiglia(0.33,"CocaCola")
    b2 = bottiglia(0.33,"Acqua")

    print(b1)
    b1.bevi(0.1)
    print(b1)
    d  = distributore(b1, b2)
    print(d)


    
