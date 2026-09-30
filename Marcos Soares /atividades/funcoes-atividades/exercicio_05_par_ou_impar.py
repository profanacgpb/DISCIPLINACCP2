def verificar_par(numero):
    return numero % 2 == 0


if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        if verificar_par(numero):
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
    except ValueError:
        print("Digite um número inteiro válido.")
