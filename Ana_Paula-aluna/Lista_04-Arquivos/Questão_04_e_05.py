#Questão 4 — Números
#Crie numeros.txt, escreva os números de 1 a 20, um por linha, e depois leia e mostre os números.

arquivo = open("numeros.txt", "w")
for numero in range(1, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()


#Questão 5 — Append
#Utilizando o arquivo da questão anterior: 

# a) adicione os números de 21 a 30; 
arquivo = open("numeros.txt", "a")
for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")
arquivo.close()

# b) leia o arquivo; 
arquivo = open("numeros.txt", "r")

# c) mostre todos os números.
for linha in arquivo:
    print(linha.strip())

arquivo.close()