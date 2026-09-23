def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero."

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
        print("Calculadora encerrada.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida.")
        continue

    numero1 = float(input("Primeiro número: "))
    numero2 = float(input("Segundo número: "))

    if opcao == "1":
        resultado = somar(numero1, numero2)
    elif opcao == "2":
        resultado = subtrair(numero1, numero2)
    elif opcao == "3":
        resultado = multiplicar(numero1, numero2)
    else:
        resultado = dividir(numero1, numero2)

    print("Resultado:", resultado)