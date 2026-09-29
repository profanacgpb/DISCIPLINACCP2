temperatura = float(input("Digite a temperatura: "))

fahrenheit = (temperatura * 9/5) + 32
celsius = (temperatura - 32) * 5/9

while True:
    print("\n===== CONVERSOR =====")
    print("1 - Celsius -> Fahrenheit")
    print("2 - Fahrenheit -> Celsius")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "3":
        print("Conversor encerrada!")
        break

    if opcao == "1":
        print(f"Resultado: {celsius}")

    elif opcao == "2":
        print(f"Resultado: {fahrenheit}")
