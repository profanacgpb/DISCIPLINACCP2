nota1, nota2, nota3 = map(float, input("Digite suas notas (1), (2), (3) (respectivamente): ").split())

def calcular_media (entrada_nota1, entrada_nota2, entrada_nota3):
    exibicao_media = (entrada_nota1 + entrada_nota2 + entrada_nota3) / 3
    return exibicao_media

exibicao_media = calcular_media (nota1, nota2, nota3)

print (f"A sua média é: {exibicao_media:.2f}")