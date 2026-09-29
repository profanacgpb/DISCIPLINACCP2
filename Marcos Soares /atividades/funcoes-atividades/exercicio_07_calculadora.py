def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def main():
    while True:
        print("\nCalculadora")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        opcao = input("Escolha uma operação: ").strip()

        if opcao == "0":
            print("Calculadora encerrada.")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            continue

        try:
            a = float(input("Digite o primeiro número: ").replace(",", "."))
            b = float(input("Digite o segundo número: ").replace(",", "."))
        except ValueError:
            print("Digite apenas valores numéricos.")
            continue

        try:
            if opcao == "1":
                resultado = somar(a, b)
            elif opcao == "2":
                resultado = subtrair(a, b)
            elif opcao == "3":
                resultado = multiplicar(a, b)
            else:
                resultado = dividir(a, b)
            print(f"Resultado: {resultado:g}")
        except ValueError as erro:
            print(erro)


if __name__ == "__main__":
    main()
