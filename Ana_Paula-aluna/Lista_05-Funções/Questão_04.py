#QUESTÃO 04 — Par ou ímpar
#Crie verificar_par(numero). Retorne True se o número for par e False caso contrário. Use o resultado para apresentar uma mensagem ao usuário

def verificar_par(numero):
    if numero%2 == 0:
        resultado = True
    else:
        resultado = False
    print(resultado)

numero = int(input("Digite um número inteiro: "))

verificar_par(numero)