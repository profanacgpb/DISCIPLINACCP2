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


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def menu():
    while True:
        print("\n========== CALCULADORA ==========")
        print("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "5":
            print("Calculadora encerrada.")
            break
        if opcao not in {"1", "2", "3", "4"}:
            print("Opção inválida.")
            continue

        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")
        operacoes = {"1": somar, "2": subtrair, "3": multiplicar, "4": dividir}
        resultado = operacoes[opcao](a, b)

        if resultado is None:
            print("Não é possível dividir por zero.")
        else:
            print(f"Resultado: {resultado:g}")


if __name__ == "__main__":
    menu()
