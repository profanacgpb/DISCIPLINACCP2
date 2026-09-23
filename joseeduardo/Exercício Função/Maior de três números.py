def maior_numero(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    return maior


numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))
numero3 = float(input("Terceiro número: "))

print("Maior número:", maior_numero(numero1, numero2, numero3))