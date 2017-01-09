'''


CLASSI return SELF e assert() !!!!


def setWidth(self, value):
    assert(isinstance(value, int))
    assert(value>=0)
    self.__width = value
    return self

def setHeight(self, value):
    assert(isinstance(value, int))  <--- verifica se esiste il valore e se è int
    assert(value>=0)                <--- altrimenti il valore di default è 0
    self.__height = value
    return self

img1.setWidth(2000).setHeight(3000)  <------------  in questo caso è possibile in cscata richiamare miù metodi   



'''


class num_comp:
    parte_reale = 0
    parte_immaginaria = 0

    def somma(self,num):
        self.parte_reale = self.parte_reale + num.parte_reale
        self.parte_immaginaria = self.parte_immaginaria + num.parte_immaginaria
        
    def stampa(self):
        print(str(self.parte_reale)+"+"+str(self.parte_immaginaria)+"i")


n1=num_comp()
n1.parte_reale=1
n1.parte_immaginaria=1

n2=num_comp()
n2.parte_immaginaria=2
n2.parte_reale=3

n1.somma(n2)
n1.stampa()


'''

OVERLOADING DEGLI OPERATORI


Ho dichiarato una funzione speciale, denominata “__add__“, in grado di effettuare
l’overloading (la sostituzione) dell’operatore ADD (+)


'''


class num_comp_overloading:
      parte_reale = 0
      parte_immaginaria = 0

      def __add__(self,num):
          ris = num_comp_overloading()
          ris.parte_reale= self.parte_reale+num.parte_reale
          ris.parte_immaginaria=self.parte_immaginaria+num.parte_immaginaria
          return ris
      def stampa(self):
          print(str(self.parte_reale)+"+"+str(self.parte_immaginaria)+"i")

n1=num_comp_overloading()
n1.parte_reale=1
n1.parte_immaginaria=7

n2=num_comp_overloading()
n2.parte_reale=1
n2.parte_immaginaria=7

r=n1+n2
r.stampa()


     