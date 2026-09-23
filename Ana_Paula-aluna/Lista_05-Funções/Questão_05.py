#QUESTÃO 05 — Calculando a média
#Crie calcular_media(n1, n2, n3) e verificar_situacao(media). Retorne “Aprovado” para média ≥7, “Recuperação” para média entre 5 e 6.9 e “Reprovado” para média < 5.

def calcular_media(n1, n2, n3):
    media = (n1+n2+n3)/3
    return media


def verificar_situacao(media):
    if media>=7:
        resultado = "Aprovado"
    elif media<5: 
        resultado = "Reprovado"
    else:
        resultado = "Recuperação"
    return resultado


nome = input("Digite seu nome: ")
n1 = float(input("Digite a Nota 1: "))
n2 = float(input("Digite a Nota 2: "))
n3 = float(input("Digite a Nota 3: "))

media = calcular_media(n1, n2, n3)
resultado = verificar_situacao(media)

print("\n")
print(f"Aluno: {nome}")
print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Nota 3: {n3}")
print(f"Média: {media:.1f}")
print(f"Situação: {resultado}")