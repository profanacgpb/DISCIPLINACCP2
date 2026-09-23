def verificar_npar(numero):
    if numero % 2 == 0:
        return True
    return False

num = int(input("Digite um número: "))

if verificar_npar(num):
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")