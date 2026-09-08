#QUESTÃO 06 - Maior de idade

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade utilizando um número inteiro: "))

if idade >= 18:
    print('\nVocê é MAIOR de idade.')

elif idade <= 0:
    print('Idade Inválida!')

else:
    print('\nVocê é MENOR de idade.')