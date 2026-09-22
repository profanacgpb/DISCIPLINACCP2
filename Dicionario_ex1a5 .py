#Questão 1
aluno = {
    "nome" : "Carlos",
    "idade" : 21,
    "curso" : "CC",
    "cidade" : "Campina Grande"
}
print(aluno)
print(aluno["nome"])
print(aluno["curso"])

#Questão 2
aluno["idade"] = 22
aluno["curso"] = "Energias Renovaveis"
print(aluno)

#Questão 3
aluno["email"] = "carlos@gmail.com"
aluno["telefone"] = "(83) 99999-9999"
print(aluno)

#Questão 4
aluno.pop("telefone")
print(aluno)

if "email" in aluno:
    print

