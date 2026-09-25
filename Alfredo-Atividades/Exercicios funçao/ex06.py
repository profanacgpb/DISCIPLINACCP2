a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a >= b:
    if a >= c:
        maior = a
    else:
        maior = c
else:
    if b >= c:
        maior = b
    else:
        maior = c

print("O maior número é:", maior)