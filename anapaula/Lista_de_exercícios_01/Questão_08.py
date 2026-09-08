#QUESTÃO 08 - Número positivo ou negativo

numero = int(input('Digite um número inteiro: '))

if numero>0:
    print('\nO número digitado é positivo.')

elif numero<0:
    print('\nO número digitado é negativo.')
else: 
    print('\nO número digitado foi zero e, portanto, NEUTRO.')