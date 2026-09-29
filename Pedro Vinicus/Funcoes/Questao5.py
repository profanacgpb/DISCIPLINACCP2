nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3= float(input("Digite sua terceira nota:"))

def media(nota1,nota2,nota3):
    return (nota1 + nota2 +nota3)/3
    
def situacao(Valor_media):
    if Valor_media >= 7:
        print("Situação:Aprovado")
    elif Valor_media >=6:
        print("Situção:Recuperação")
    else:
        print("Situação:Reprovado")

resultado = media(nota1,nota2,nota3)
print(f"Media:{resultado:.1f}")
situacao(resultado)   