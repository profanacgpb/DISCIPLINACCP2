#Exercício 8 — Sistema de notas
def ler_notas(n1,n2,n3,n4):
    print(f"Suas notas são {n1, n2, n3, n4}")

def calcular_media(n1,n2,n3,n4):
    return (n1 + n2 + n3 + n4) / 4

def verificar_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, situacao):
    print(f"Seu nome é {nome}")
    print(f"Sua media é {media}")
    print(f"Sua situação é {situacao}")

print("==============Sistema de Notas============")
nome = input("Informe o seu nome: ")
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
n4 = float(input("Digite a sua quarta nota: "))

media = calcular_media(n1,n2,n3,n4)
situacao = verificar_situacao(media)

exibir_resultado(nome, media, situacao)