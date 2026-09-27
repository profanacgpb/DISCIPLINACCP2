def calcular_media(n1,n2,n3):
    return(n1+n2+n3) /3
def verificar_situação(media):
    if media >=7:
        return "aprovado"
    elif media >=5:
        return "recuperação"
    else:
        return "reprovado"
aluno=input("aluno: ")

nota1= float(input("nota 1:"))
nota2= float(input("nota 2:"))
nota3= float(input("nota 3:"))

media= calcular_media(nota1,nota2,nota3)
situação= verificar_situação(media)

print("\n aluno", aluno)
print("nota 1:", nota1)
print("nota 2:", nota2)
print("nota 3:", nota3)
print("Média:", media)
print("situação", situação)       

    





