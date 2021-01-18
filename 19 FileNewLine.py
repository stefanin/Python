nuovaLinea = '''

prima linea
#seconda linea
treza linea
'''

with open("EsempioFile.txt", "a") as vFile:
  vFile.write(nuovaLinea)
  vFile.write("\n")