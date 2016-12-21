'''

MODULI : file che possono contenere funzioni, classi con estensione '.py'
In “bundle” con Python abbiamo moduli che forniscono funzioni utili per risolvere diverse
problematiche. I file devo risiedere nella stessa directori del programma

import libreria :comando per imnportare il modulo DICHIARE ALL'INIZIO

Le funzioni nella libreria richideono la dot-notation

libreria.funzione()

per evitare la dot-notation :

from libreria import funzione

in questo caso posso utilizzre solo la funzione dichiarata


se voglio utilizzare la libreia dot-notation e la funzione :

import libreria
from libreria import funzione

Se voglio utilizzare tuute lr finzioni senza la dot-notation posso :

from libreria import *

OPPURE

from libreria import a,b,c



il compilatote python crea un file compilato '.pyc', controlla il timestamp del file 
.py con il file .pyc e decide se ricompilarlo o eseguire il bytecode 

Moduli standard :
string 
sys 
os 



NAMESPACE :

Il modulo ha un insieme di nomi (variabili e funzioni), il comando 'import' importa 
dal namespace modulo.py al namespace del notro programma

'''

print(dir()) #elenca i nomi nel namespace
print()
print(dir(__doc__.count))

from datetime import datetime
import time
d=datetime.now()
print(d)
#time.sleep(5)
print((datetime.now() - d).seconds)



'''

PROGRAMMAZIONE OO

Nell’approccio “a oggetti” ci si focalizza sull’interazione di elementi (oggetti) che comunicano (scambiano messaggi) tra loro

Classe :  è una collezione di uno o più oggetti contenenti
un insieme uniforme di attributi e servizi, insieme ad una
descrizione circa come creare nuovi elementi della
classe stessa

Oggetto è dotato di stato, comportamento ed
identità; la struttura ed il comportamento di oggetti
simili sono definiti nelle loro classi comuni; i termini
istanza ed oggetto sono intercambiabili. Di fatto occupa memoria quando viene istanziato


Ci sono tre parti particolarmente importanti:
1. OOP utilizza un insieme di oggetti (non algoritmi, e gli oggetti sono la
parte fondamentale della costruzione logica);
2. ogni oggetto è istanza di una classe;
3. ogni classe è legata alle altre attraverso una relazione detta eredità.


CARATTERISTICHE OO


• Astrazione
focalizzare l’attenzione su una visione esterna di un oggetto, ovvero le classi
• Incapsulamento
l’aggregazione di informazioni delle classi, tipicamente la struttura di un oggetto viene mantenuta nascosta
• Gerarchia
specializzare il codice 
• Modularità
è possibile definire dei singoli oggetti riutilizzabili
'''