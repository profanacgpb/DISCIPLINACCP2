#QUESTÃO 03 — Calculadora de soma 
# Crie somar(a, b) para retornar a soma. No programa principal, solicite dois números, chame a função, armazene e exiba o resultado. Primeiro número: 15 Segundo número: 8 Resultado: 23

def somar(a,b):
    return a+b

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

resultado = somar(num_1, num_2)
print(f"Resultado: {resultado}")
