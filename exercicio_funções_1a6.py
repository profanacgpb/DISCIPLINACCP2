#Questão 1
def apresentar():
    print("Bem-vindo à disciplina de Programação!")
#programa principal
apresentar()


#Questão 2
def saudação():
     print(f"Olá, {nome}! Seja bem-vindo(a) à programação!")
#programa principal
nome = input('Digite seu nome:')
saudação()


#Questão 3
def soma(a, b):
     return resultado = float(a) + float(b)
#programa principal
n1 = input('Primeiro numero:')
n2 = input('Segundo numero:')
print("resultado:", resultado)


#Questão 4
def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#programa principal 
numero= int(input('Digite um numero:'))
resultado= verificar_par(numero)
if resultado: 
    print('O numero é par!')
else:
    print('O numero e impar!')


#Questão 5
def calcular_media(n1, n2, n3):
    return float(n1) + float(n2) + float(n3) /3

def verificar_situação(media):
    if media >== 7:
        return aprovado
    else:
        return reprovado
        
#programa principal
n1= input ("Nota 1:")
n2= input ("Nota 2:")
n3= input ("Nota 3:")
media= calcular_media(n1, n2, n3)
print(f"Media: {media}")
print(verificar_situação(media))
