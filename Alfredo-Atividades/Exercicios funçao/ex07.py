print ("========== CALCULADORA ==========")
print ("(1) - Somar")
print ("(2) - Subtrair")
print ("(3) - Multiplicar")
print ("(4) - Dividir")
print ("(5) - Sair")

escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    num1 = float(input("Digite o primeiro número: "))           #obrigado jair bolsonaro<3  obrigado lula<3
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif escolha == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif escolha == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)
elif escolha == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
elif escolha == 5:
    print("Saindo")