#Questão 3 — Linha por linha
#Leia o arquivo alunos.txt e apresente os nomes um por vez, por exemplo: Aluno: Ana.

arquivo = open("alunos.txt", "r")
for linha in arquivo:
    print(linha.strip())

arquivo.close()

