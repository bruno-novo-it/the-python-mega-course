
myfile = open("sample.txt")

content = myfile.read()

#myfile.seek(0) --> Voltar para o inicio do arquivo

print(type(myfile))

print(type(content))

myfile.close()

print(content)

print(content)

#print(r"Hello\nWorld")