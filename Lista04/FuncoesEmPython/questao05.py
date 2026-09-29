def calcular_media(n1,n2,n3):
    return (n1 + n2 + n3) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 6.9:
        return "Recuperação"
    else:
        return "Reprovado"

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = calcular_media(n1,n2,n3)
situacao = verificar_situacao(media)

print(f"Média {media}")
print(f"Situação {situacao}")