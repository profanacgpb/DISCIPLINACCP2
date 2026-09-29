def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


while True:
    print("\n========== CALCULADORA ==========")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Programa encerrado.")
        break

    if opcao in ["1", "2", "3", "4"]:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", somar(a, b))

        elif opcao == "2":
            print("Resultado:", subtrair(a, b))

        elif opcao == "3":
            print("Resultado:", multiplicar(a, b))

        elif opcao == "4":
            resultado = dividir(a, b)

            if resultado is None:
                print("Erro: não é possível dividir por zero.")
            else:
                print("Resultado:", resultado)
    else:
        print("Opção inválida.")
