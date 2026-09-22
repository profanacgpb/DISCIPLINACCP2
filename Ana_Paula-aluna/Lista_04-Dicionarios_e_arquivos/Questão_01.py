#QUESTÃO 1 — Primeiro arquivo
#Crie um arquivo chamado alunos.txt e escreva nele os nomes de 5 alunos.

arquivo = open("alunos.txt", "w")

arquivo.write("Ana Paula\n")
arquivo.write("Sergio\n")
arquivo.write("Bruna\n")
arquivo.write("Lucas\n")
arquivo.write("Alex\n")

arquivo.close()



