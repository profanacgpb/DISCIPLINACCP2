# a. Escreva no arquivo os números de 1 a 10
arquivo = open("numeros.txt", "w")

for numero in range(1, 11):
    arquivo.write(str(numero) + "\n")

arquivo.close()


# b. Imprima na tela todos os números do arquivo
arquivo = open("numeros.txt", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()


# c. Escreva no arquivo os números de 11 a 20,
# substituindo os números que estavam antes
arquivo = open("numeros.txt", "w")

for numero in range(11, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()


# d. Escreva no arquivo os números de 21 a 30,
# adicionando no final sem apagar os anteriores
arquivo = open("numeros.txt", "a")

for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")

arquivo.close()


# e. Imprima na tela todos os números do arquivo novamente
arquivo = open("numeros.txt", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()


# f. Imprima na tela todos os números linha por linha
arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()