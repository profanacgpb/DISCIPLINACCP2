#QUESTÃO 12 - Contagem Personalizada

numero = int(input('Digite um número inteiro positivo: '))

if numero<=0:
    print('Número inválido!')
else:
    for numero in range(1,numero+1):
        print(numero)