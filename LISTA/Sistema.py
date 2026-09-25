#10- Crie um menu:
# 1 - Cadastrar aluno
# 2 - Listar alunos
# 3 - Sair
# A opção 1 grava o nome no arquivo; a opção 2 lê e apresenta os alunos; a opção 3 encerra o programa.
while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        with open("sistema.txt", "a") as arquivo:
            arquivo.write(nome + "\n")
        print("Aluno cadastrado!")
        
    elif opcao == "2":
        print("\n=== Lista de Alunos ===")
        with open("sistema.txt", "r") as arquivo:
            print(arquivo.read().strip())
            
    elif opcao == "3":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")
