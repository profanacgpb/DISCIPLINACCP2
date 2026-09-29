def verificar_par(numero):
    return numero % 2 == 0


def sera_par():
    numero = ler_inteiro("Digite um número inteiro: ")
    if verificar_par(numero):
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
