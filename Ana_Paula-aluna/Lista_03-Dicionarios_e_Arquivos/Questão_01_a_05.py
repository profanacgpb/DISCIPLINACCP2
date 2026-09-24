#LISTA DE EXERCÍCIOS: DICIONÁRIO E ARQUIVOS - AULA DO DIA 15/09/2026
#QUESTÃO 1 — Cadastro de aluno
#Crie um dicionário chamado aluno contendo nome, idade, curso e cidade.

aluno = {
    "nome" : "Ana",
    "idade" : 29,
    "curso" : "Ciência da Computação",
    "cidade" : "Campina Grande"
}
print("QUESTÃO 1:")
#a) Imprima o dicionário completo.
print(aluno)

#b) Imprima apenas o nome.
print(aluno["nome"])

#c) Imprima apenas o curso.
print(aluno["curso"])



print("\nQUESTÃO 2:")
#QUESTÃO 2 — Alteração Utilize o dicionário da questão anterior.
#a) Altere a idade do aluno.
aluno["idade"] = 37

#b) Altere o curso.
aluno["curso"] = "Matemática"

#c) Imprima o dicionário novamente.
print(aluno)



print("\nQUESTÃO 3:")
#QUESTÃO 3 — Nova informação
#Adicione ao dicionário as informações email e telefone. Depois imprima todas as informações.
aluno["email"] = "email_do_aluno@gmail.com"
aluno["telefone"] = 83999999999

print("\nLista final:")
print(aluno)



print("\nQUESTÃO 4:")
#QUESTÃO 4 — Remoção
#Remova a informação telefone do dicionário e imprima o resultado.
aluno.pop("telefone")
print(aluno)



print("\nQUESTÃO 5:")
#QUESTÃO 5 — Questão 5 — Verificação
#Crie um programa que verifique se a chave email existe. Se existir, mostre “E-mail cadastrado.”; caso contrário, mostre “E-mail não cadastrado.”
if "email" in aluno:
    print("E-mail cadastrado")
else:
    print("E-mail não cadastrado")