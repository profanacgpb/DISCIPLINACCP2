def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return None
    return a / b


def exibir_menu_calculadora():
    print("========== CALCULADORA ==========")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")


def questao_07():
    operacoes = {1: somar, 2: subtrair, 3: multiplicar, 4: dividir}
    while True:
        exibir_menu_calculadora()
        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 5:
            print("Encerrando a calculadora...")
            break
        elif opcao in operacoes:
            a = ler_numero("Primeiro número: ")
            b = ler_numero("Segundo número: ")
            resultado = operacoes[opcao](a, b)
            if resultado is None:
                print("Erro: não é possível dividir por zero!")
            else:
                print(f"Resultado: {resultado}")
        else:
            print("Opção inválida!")