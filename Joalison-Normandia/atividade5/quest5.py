def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

aluno = input("Aluno: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = calcular_media(n1, n2, n3)
situacao = verificar_situacao(media)

print(f"Média: {media}")
print(f"Situação: {situacao}")