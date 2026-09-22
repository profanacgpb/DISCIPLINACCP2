arquivo = open("numeros.txt", "a")

for numero in range(20,41):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")
conteudo = arquivo.read()
print (conteudo)

arquivo.close()

arquivo = open("numeros.txt", "r")

for numero in arquivo:
    print(numero.strip())

arquivo.close()

