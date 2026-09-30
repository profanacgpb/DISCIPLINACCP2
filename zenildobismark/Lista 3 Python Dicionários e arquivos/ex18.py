# Crie um menu: 
# 1 - Cadastrar aluno 
# 2 - Listar alunos 
# 3 - Sair 
# A opção 1 grava o nome no arquivo; 
# a opção 2 lê e apresenta os alunos; 
# a opção 3 encerra o programa.

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        aluno = input("Digite o nome do aluno: ")
        with open('alunos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{aluno}\n")
        print("Aluno cadastrado com sucesso!")

    elif opcao == '2':
        try:
            with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
                alunos = arquivo.readlines()
                
            if not alunos:
                print("Nenhum aluno cadastrado ainda.")
            else:
                print("\n--- LISTA DE ALUNOS ---")
                for i, aluno in enumerate(alunos, start=1):
                    print(f"{i}. {aluno.strip()}")
        except FileNotFoundError:
            print("O arquivo ainda não existe. Cadastre um aluno primeiro.")

    elif opcao == '3':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")