# Crie calcular_media(n1, n2, n3) e verificar_situacao(media). 
# Retorne “Aprovado” para média ≥ 7, “Recuperação” para média entre 5 e 6.9 e “Reprovado” para média < 5.

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) /3
    if media >= 7:
        return "Aprovado"
    elif media >= 5 & media <= 6.9:
        return "Recuperação"
    else:
        return "Reprovado"

print(calcular_media(7, 7.1, 7))