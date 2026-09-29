def ler_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    return n1, n2, n3


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_resultado(media, situacao):
    print("\n===== RESULTADO =====")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


# Programa principal
n1, n2, n3 = ler_notas()

media = calcular_media(n1, n2, n3)

situacao = verificar_situacao(media)

exibir_resultado(media, situacao)