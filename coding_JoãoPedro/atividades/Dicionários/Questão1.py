#Cadastro de aluno
aluno = {
"nome": "João Pedro", 
"idade": 19,
"curso": "Ciência da Computação",
"cidade": "Areia"
}
print("\n")
print(aluno)

print("\n")
print(aluno["nome"])

print("\n")
print(aluno["curso"])

#Alteração
aluno ["idade"] = 20
print("\n")
print(aluno)

aluno ["curso"] = "ADS"
print("\n")
print(aluno)

#Nova informção
print("\n")
aluno ["email"] = "joaopedro.campos.cs@gmail.com"
aluno ["telefone"] = 83981010977
print(aluno)

#Remoção
del aluno["telefone"]
print(aluno)

#Verificação
if "email" in aluno:
    print("E-mail cadastrado!")
else:
    print("E-mail não cadastrado!")