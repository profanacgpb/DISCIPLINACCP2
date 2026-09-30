def verificar_par(numero):
    """Retorna True quando o número é par, e False nos demais casos."""
    return numero % 2 == 0


if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: "))
    if verificar_par(numero):
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")
