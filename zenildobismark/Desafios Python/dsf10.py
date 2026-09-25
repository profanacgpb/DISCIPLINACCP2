#Crie um cadastro simples de alunos usando uma lista e um menu de inclusão, listagem e remoção.

alunos = []

while True:
    print("-------------OPÇÕES---------------")
    print("Digite (1) para INCLUSÃO DE ALUNOS")
    print("Digite (2) para LISTAR ALUNOS")
    print("Digite (3) para REMOVER ALUNOS")
    print("Digite (4) para SAIR")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        aluno = input("Digite o nome do aluno: ")
        alunos.append(aluno)
        print(f"ALUNO {aluno} INCLUIDO COM SUCESSO")

    elif op == 2:
        if alunos == 0:
            print("NENHUM ALUNO CADASTRADO")
        else:
            print(alunos)

    elif op == 3:
        aluno = input("Digite o nome do aluno: ")
        if aluno in alunos:
            alunos.remove(aluno)
            print(f"ALUNO {aluno} REMOVIDO COM SUCESSO!")
        else:
            print("ALUNO NÃO ENCONTRADO!")

    elif op == 4:
        print("SAINDO DO SISTEMA!")
        break

    else:
        print("OPÇÃO INVÁLIDA, DIGITE OUTRA OPÇÃO NOVAMENTE!")