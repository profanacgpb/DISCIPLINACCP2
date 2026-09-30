# Crie maior_numero(a, b, c) para retornar o maior de três números. Não utilize max().

def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maior_numero(7, 8, 9))