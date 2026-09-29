#Exercício 6 — Maior número
def maior(a,b):
    if a > b:
        return "maior"
    elif b > a:
        return "maior"
    else:
        return "Os dois são iguais"

maior1 = maior(4,5)
print(maior1)

maior2 = maior(5,4)
print(maior2)

maior3 = maior(5,5)
print(maior3)