# 1. Crie um dicionário chamado aluno contendo nome, idade, curso e cidade:

aluno = {
    "nome": "Cleitin",
    "idade": 19,
    "curso": "Ciência da Computação",
    "cidade": "Santa Cecília"
}

# a) Imprima o dicionário completo:
print (f"Dicionário Completo: ")
for nome, atributo in aluno.items():
    print (f"{nome}, {atributo}")
print ("\n")
# b) Imprima apenas o nome:
print (aluno["nome"])

# c) Imprima apenas o curso:
print (aluno["curso"])
print ("\n")

# 2. Utilize o dicionário da questão anterior:

# a) Altere a idade do aluno:
aluno ["idade"] = 30
print ("\n")
# b) Altere o curso:
aluno ["curso"] = "ADS"

# c) Imprima o dicionário novamente:
print (aluno)
print ("\n")
# 3. Adicione ao dicionário as informações email e telefone. Depois imprima todas as informações.

aluno.update({"email": "cleitin123@gmail.com", "telefone": 839876435642})

print (aluno)

# 4. Remova a informação telefone do dicionário e imprima o resultado:

aluno.pop ("telefone")

print (aluno)
print ("\n")
# 5. Crie um programa que verifique se a chave email existe. Se existir, mostre “E-mail cadastrado.”; caso contrário, mostre “E-mail não cadastrado.”

if "email" in aluno: # in => em
    print ("Email Cadastrado")
else:
    print ("Email Não Cadastrado")
