def calculadora(numero1, numero2, operacao):

    if operacao == "1":
        return numero1 + numero2

    elif operacao == "2":
        return numero1 - numero2

    elif operacao == "3":
        return numero1 * numero2

    elif operacao == "4":
        if numero2 == 0:
            return "Não é possível dividir por zero."
        return numero1 / numero2

    else:
        return "Opção inválida."


while True:
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Calculadora encerrada!")
        break

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = calculadora(numero1, numero2, opcao)

    print(f"Resultado: {resultado}" )
