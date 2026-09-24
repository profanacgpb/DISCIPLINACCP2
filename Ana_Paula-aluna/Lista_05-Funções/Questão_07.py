#QUESTÃO 07 — Calculadora utilizando funções
#Crie somar(a,b), subtrair(a,b), multiplicar(a,b) e dividir(a,b). Faça um menu com 1-Somar,
#2-Subtrair, 3-Multiplicar, 4-Dividir e 5-Sair. Trate divisão por zero.

def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

print("- NÚMEROS QUE SERÃO UTILIZADOS -")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))

print("\n========== CALCULADORA ==========")
print(" 1 - Somar")
print(" 2 - Subtrair")
print(" 3 - Multiplicar")
print(" 4 - Dividir")
print(" 5 - Sair")

opcao_escolhida = int(input("\nDigite uma opção: "))

while opcao_escolhida in (1, 2, 3, 4, 5):
    if opcao_escolhida == 1:
        resultado = somar(num_1, num_2)
        print(f"Resultado: {num_1} + {num_2} = {resultado:.1f}")

    elif opcao_escolhida == 2:
        resultado = subtrair(num_1, num_2)
        print(f"Resultado: {num_1} - {num_2} = {resultado:.1f}")

    elif opcao_escolhida == 3:
        resultado = multiplicar(num_1, num_2)
        print(f"Resultado: {num_1} x {num_2} = {resultado:.1f}")

    elif opcao_escolhida == 4:
        if num_2 != 0:
            resultado = dividir(num_1, num_2)
            print(f"Resultado: {num_1} : {num_2} = {resultado:.1f}")
        else:
            print("Não é possível realizar divisão por zero.")

    elif opcao_escolhida == 5:
        break

    opcao_escolhida = int(input("\nDigite outra opção: "))

print("- Fim do programa -")
