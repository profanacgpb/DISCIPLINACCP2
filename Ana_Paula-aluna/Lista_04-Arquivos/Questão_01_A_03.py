#QUESTÃO 1 — Primeiro arquivo
#Crie um arquivo chamado alunos.txt e escreva nele os nomes de 5 alunos.

arquivo = open("alunos.txt", "w")

arquivo.write("Ana Paula\n")
arquivo.write("Sergio\n")
arquivo.write("Bruna\n")
arquivo.write("Lucas\n")
arquivo.write("Alex\n")

arquivo.close()


#QUESTÃO 2 — Leitura
#Leia o arquivo alunos.txt e imprima todos os nomes na tela.
arquivo = open("alunos.txt", "r")
conteudo = arquivo.read()
print(conteudo)

arquivo.close()


#Questão 3 — Linha por linha
#Leia o arquivo alunos.txt e apresente os nomes um por vez, por exemplo: Aluno: Ana.

arquivo = open("alunos.txt", "r")
for linha in arquivo:
    print(linha.strip())

arquivo.close()



