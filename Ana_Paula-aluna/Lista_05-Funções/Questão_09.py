#QUESTÃO 09 — Sistema de cadastro de alunos
#Crie um sistema com 1-Cadastrar, 2-Listar, 3-Buscar e 4-Sair. Cada aluno possui Nome, Idade e Curso. Use uma lista de dicionários e as funções cadastrar_aluno(), listar_alunos(), buscar_aluno() e menu().

lista_de_alunos = []

def cadastrar_aluno():
    print("CADASTRO DE ALUNOS")
    nome = input("Digite o nome do aluno (LETRAS MAIÚSCULAS)3: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")
    novo_aluno = {
        "Nome": nome,
        "Idade": idade,
        "Curso": curso
    }
    lista_de_alunos.append(novo_aluno)


def listar_alunos():
    print("ALUNOS CADASTRADOS:")
    for aluno in lista_de_alunos:
        print(aluno["Nome"])

#def menu():
#    print()


def buscar_aluno():
    nome = input(("Qual aluno você deseja buscar (LETRAS MAIÚSCULAS)? "))
    for aluno in lista_de_alunos:
        aluno = aluno["Nome"]
        
        if nome == aluno:
            print("Aluno cadastrado!")
            break
    else:
        print("Aluno NAO cadastrado!")


print("----- SISTEMA DE CADASTRO -----")
print("1 - Cadastrar")
print("2 - Listar")
print("3 - Buscar")
print("4 - Sair")

opcao = int(input("\nEscolha uma opção: "))

while True:
    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        buscar_aluno()
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")

    opcao = int(input("\nEscolha outra opção: "))
