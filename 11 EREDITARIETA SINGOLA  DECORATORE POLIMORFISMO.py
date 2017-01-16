'''


EREDITARIETA'


singola e multipla



Singola


'''




class Corsi:
    titolo=""
    descrizione=""
    def stampa(self):
        print(self.titolo,self.descrizione)


class persona:
    nome = ""
    cognome = ""
    indirizzo = ""
    __telefono = "" #Per indicare di tenere protetti i dati membri e quindi realizzare veramente l’incapsulamento, si deve anteporre al nome della variabile i caratteri “__” ( 2 underscore)
    stato_civile = ""
    corso = Corsi()

    def __init__(self,n,c,i=""):# COSTRUTTORE  __init__ metodo standard per inizializzare l'oggetto
        self.nome=n
        self.cognome=c
        self.indirizzo =i
    def cambia_indirizzo(self,s): # uyilizzo self per poter assegnare la variabile
        self.indirizzo = s
    def cambia_telefono(self,s):
        self.telefono = s
    def cambia_stato_civile(self,s):
        self.stato_civile = s
    def stampa(self):
        print(self.nome,self.cognome,self.indirizzo,self.stato_civile,self.__telefono)
        self.corso.stampa()

class studente (persona): # ecco l’ereditarietà!
    scuola = ""
    classe = 0
    def cambia_scuola(self,s):
        self.scuola = s

    def promosso(self):
        if self.classe == 5:
            print("scuola finita")
        else:
            self.classe = self.classe + 1
    def stampa(self):
        #print(self.nome,self.cognome,self.indirizzo,self.stato_civile)
        super().stampa()# ___________________________________________________EREDITA IL METODO PADRE !!!!!
        print(self.scuola,str(self.classe))
        


p1 = studente("Gino","Rozzi")
p1.scuola="prima"
p1.classe=2
p1.stampa()






class Shape:
    '''Un oggetto di tipo Shape rappresenta una figura geometrica generica'''
    @property
    def area(self):
        '''Restituisce l'area della figura'''
        pass
    @property
    def perimeter(self):
        '''Restituisce il perimetro della figura'''
        pass
    @property
    def name(self):
        return getattr(self, '_name', 'Untitled')
        # restituisce l'attributo _name se esiste, altrimenti
        'Untitled'


class Rectangle(Shape):
    def __init__(self, width, height, name="A rectangle"):
        self._width=width
        self._height=height
        self._name=name
    @property #------------------------------ con il decoratote trasformo il metodo in valore
    def perimeter(self):
        '''perimetro'''
        return 2*(self._height+self._width)
    @property
    def area(self):
        return self._height * self._width


class Circle(Shape):
    def __init__(self, radius):
        self._radius=radius
    @property
    def perimeter(self):
        return self._radius*2
    @property
    def area(self):
        return self._radius ** 2




a= Rectangle(10,15)
print(str(a.area))
print(str(a.perimeter))
print(type(a))



'''

POLIMORFISMO

Il polimorfismo fa sì che gli oggetti si comportino in maniera diversa a seconda della classe a cui appartengono,
quando viene invocato uno specifico metodo (o quando viene richiesto l'accesso ad una proprietà).

'''

shapes=[
    Circle(5),
    Rectangle(9,10),
    Rectangle(11,21,'R1'),
]
for s in shapes:
    print(str(s.perimeter))


'''
EREDITARITA' MULTIPLA

è implementata ma non usata a causa della complessità

'''
