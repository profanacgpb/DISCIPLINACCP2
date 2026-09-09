#Crie um menu textual que permaneça ativo até o usuário escolher “Sair”.

while True:
    print("--------Escolha uma opção---------")
    print("(1) Carro")
    print("(2) Moto")
    print("(3) Avião")
    print("(4) Barco")
    print("(5) Sair")

    opcao = int(input("Digite uma das opções acima: "))

    if opcao == 1:
        print("Você escolheu Carro.")

    elif opcao == 2:
        print("Você escolheu Moto.")

    elif opcao == 3:
        print("Você escolheu Avião.")

    elif opcao == 4:
        print("Você escolheu Barco.")

    elif opcao == 5:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")