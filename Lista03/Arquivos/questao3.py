#Questão 3 - Linha por linha
arquivo2 = open("dados.txt", "r")
for linha in arquivo2:
    print(linha.strip())

    arquivo2.close()