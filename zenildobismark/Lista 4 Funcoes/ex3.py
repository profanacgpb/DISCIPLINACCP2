# Crie somar(a, b) para retornar a soma. No programa principal, 
# solicite dois números, chame a função, armazene e exiba o resultado.

def somar(a, b):
    return a + b


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = somar(a, b)

print(f"O primeiro número é: {a}")
print(f"O segundo número é: {b}")
print(f"A soma é: {soma}")
