def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media < 5:
        return "Reprovado"
    else:
        return "Recuperação"

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media)

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")