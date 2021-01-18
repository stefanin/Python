vFile = open("EsempioFile.txt", "r")

lines = vFile.readlines()
vFile.close()

new_file = open("EsempioFile.txt", "w")
for line in lines:
    if line.strip("\n") != "treza linea":
        new_file.write(line)

new_file.close()