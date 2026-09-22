Aluno={"nome": ".",
       "Idade": ".",
       "Curso": "."}
Aluno["nome"]=input("Digite seu nome: ")
Aluno["Idade"]=input("Digite sua idade: ")
Aluno["Curso"]=input("Digite seu curso: ")
Aluno2={"nome": ".",
       "Idade": ".",
       "Curso": "."}
Aluno2["nome"]=input("Digite seu nome: ")
Aluno2["Idade"]=input("Digite sua idade: ")
Aluno2["Curso"]=input("Digite seu curso: ")

lista=[Aluno]
lista2=[Aluno2]
print(lista)

with open("Alunos.txt", "w")as Alunos:
   Alunos.write(str(lista)+"\n")
   Alunos.write(str(lista2))
