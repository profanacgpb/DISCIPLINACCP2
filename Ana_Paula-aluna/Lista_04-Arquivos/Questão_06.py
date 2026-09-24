#QUESTÃO 6 — Substituição
#Crie mensagem.txt, escreva “Primeira mensagem” e depois, usando o modo w, substitua por “Nova mensagem”. Leia o arquivo e verifique o resultado.

arquivo = open("mensagem.txt", "w")
arquivo.write("Primeira mensagem")
arquivo.close()

#Apresentação do arquivo inicial
arquivo = open("mensagem.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#ALTERAÇÃO DO ARQUIVO
arquivo = open("mensagem.txt", "w")
arquivo.write("Nova mensagem")
arquivo.close()

arquivo = open("mensagem.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


