def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = calcular_media(nota1, nota2, nota3)

situacao = verificar_situacao(media)

print("Média:", media)
print("Situação:", situacao)