def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


print("===== CALCULADORA =====")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma operação: "))

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", somar(a, b))

elif opcao == 2:
    print("Resultado:", subtrair(a, b))

elif opcao == 3:
    print("Resultado:", multiplicar(a, b))

elif opcao == 4:
    if b != 0:
        print("Resultado:", dividir(a, b))
    else:
        print("Não é possível dividir por zero.")

else:
    print("Opção inválida.")