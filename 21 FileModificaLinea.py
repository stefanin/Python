vFile = open("EsempioFile.txt", "r")

lines = vFile.readlines()
vFile.close()

new_file = open("EsempioFile.txt", "w")
for line in lines:
    if line.strip("\n") == "#seconda linea":
        new_file.write("seconda linea")
    else:
        new_file.write(line)

new_file.close()