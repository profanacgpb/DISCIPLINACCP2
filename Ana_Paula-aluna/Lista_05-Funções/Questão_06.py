#QUESTÃO 06 — Maior de três números
#Crie maior_numero(a, b, c) para retornar o maior de três números. Não utilize max().

def maior_numero(a, b, c):
    numeros = [a, b, c]
    maior = 0
    for i in numeros:
        if i>maior:
            maior = i
    return maior


a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

maior_valor = maior_numero(a, b, c)

print(f"Maior número: {maior_valor}")
