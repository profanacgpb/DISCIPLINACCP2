# Crie somar(a,b), subtrair(a,b), multiplicar(a,b) e dividir(a,b). 
# Faça um menu com 1-Somar, 2-Subtrair, 3-Multiplicar, 4-Dividir e 5-Sair. Trate divisão por zero.

def somar(a, b):
    return f"A soma é: {a + b}"

def subtrair(a, b):
    return f"A subtração é: {a - b}"

def multiplicar(a, b):
    return f"A multiplicação é: {a * b}"

def dividir(a, b):
    return f"A divisão é: {a % b}"

while True:
    print("------------DIGITE A OPÇÃO DESEJADA--------------")
    print("Digite (1) para SOMAR")
    print("Digite (2) para SUBTRAIR")
    print("Digite (3) para MULTIPLICAR")
    print("Digite (4) para DIVIDIR")
    print("Digite (5) para SAIR")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(somar(n1, n2))

    elif op == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(subtrair(n1, n2))

    elif op == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(multiplicar(n1, n2))

    elif op == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(dividir(n1, n2))

    elif op == 5:
        print("Programa ENCERRADO!")
        break

    else:
        print("Opção Inválida!")
    

    

