#QUESTÃO 2 — Leitura
#Leia o arquivo alunos.txt e imprima todos os nomes na tela.
arquivo = open("alunos.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()