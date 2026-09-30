#Questão 1- Cadastro do Aluno
Aluno={"Nome" : "Ronne",
    "Idade": "19",
    "cidade" : "Campina Grande",
    "Curso" : "C.C."}
print(Aluno)
print(Aluno["Nome"])
print(Aluno["Curso"])

#Questão 2- Alteração
Aluno["Idade"]="20"
Aluno["Curso"]="ADS"
print(Aluno)

#Questão 3- Nova informação
Aluno["Email"]="ronneraizlia@gmail.com"
Aluno["Telefone"]="83 9"
print(Aluno)

#Questão 4- Remoção
Aluno.pop("Telefone")
print(Aluno)

#Questão 5- Verificação
if "Email" in Aluno:
    print("O Email existe!")

#Questão 6- Percorrendo o dicionário 
for chave, valor in Aluno.items():
    print(valor)