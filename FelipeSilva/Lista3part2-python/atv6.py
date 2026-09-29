arquivo = open("mensagem.txt", "w")
arquivo.write("Primeira mensagem")
arquivo.close()

arquivo = open("mensagem.txt", "w")
arquivo.write("Nova mensagem")
arquivo.close()

arquivo = open("mensagem.txt", "r")

print(arquivo.read())

arquivo.close()