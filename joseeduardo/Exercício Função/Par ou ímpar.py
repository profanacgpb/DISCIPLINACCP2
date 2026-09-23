def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input("Digite um número inteiro: "))

if verificar_par(numero):
    print("O número é par.")
else:
    print("O número é ímpar.")