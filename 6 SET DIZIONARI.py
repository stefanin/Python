'''

        SET

    sono definibili come delle raccolte non ordinate di elementi univuci
    non è possibile inserire una lista
    non è contemplato l'utilizzo dell indice  nomeset[1] ---- non funziona

'''

nome_set = {'a','b','c'}
nome_set = {'a','b','c',120,(1,3,4)}

nome_set = {'a','b','c',120,120,(1,3,4)} # elimina il duplicato
print(nome_set)
print(set([1,4,4,3,5])) #convertire tupla e lista con set()
print(set('homer'))  # la stringa viene scomposta in caratteri
nome_set.add(100)
print(nome_set) # inserimento di un valore
nome_set.update([1,4,5])
print(nome_set,"update di valori nome_set.update([1,4,5])")
nome_set.pop()
print("nome_set.pop() elimina un valore casual :",nome_set)
print("nome_set.clear() cancella il set :",nome_set.clear())
a_set = {'a','b','c'}
nome_set = {'a','b','c',120,(1,3,4)}
print ("aggiungo un set a_set",a_set," nome_set || a_set :", nome_set | a_set )

x_set = {1,2,3,4,5,6}
y_set = {4,5,6,7,8,9}
print ("operazione di differenza con x_set - y_set ", x_set - y_set)
print ("ce non è simmetrica seinverto i valori y_set - x_set ", y_set - x_set)
print ("differenza simmetrica  y_set ^ x_set ",y_set," tra ",x_set, " ", y_set ^ x_set)
print ("fozenset() congela l'insiame dato ",frozenset(y_set), "l'interpetre genererà un errore se si tenta di modificare il set")



