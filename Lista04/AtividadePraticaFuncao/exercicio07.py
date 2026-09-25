#Exercício 7 — Calculadora
def somar(a,b):
    return (a+b)

def subtrair(a,b):
    return(a-b)

def multiplicar(a,b):
    return(a*b)

def dividir(a,b):
    return(a/b)

print("=====================================================")
print(" Digite o icone das operações que deseja calcular: ")
print("             ====================")
print("              Operações: + - * /")
print("=====================================================")

operacao = input("Digite aqui: ").strip()
num1 = int(input("Digite aqui o primeiro valor  a ser calculados: "))
num2 = int(input("Digite aqui o segundo valor  a ser calculados: "))

if operacao == "+":
    soma = somar(num1,num2)
    print(f"A soma desses dois números é {soma}")
elif operacao == "-":
    subtrair = subtrair(num1,num2)
    print(f"A subtração desses dois números é {subtrair}")
elif operacao == "*":
    multiplicar = multiplicar(num1,num2)
    print(f"A multiplicação desses dois números é {multiplicar}")
elif operacao == "/":
    dividir = dividir(num1,num2)
    print(f"A divisão desses dois números é {dividir}")
else:
    print("Desculpe você não pode fazer uma operação se não digitar nenhuma dessas acima!")