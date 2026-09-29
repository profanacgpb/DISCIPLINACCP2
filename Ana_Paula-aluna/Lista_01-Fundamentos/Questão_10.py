#QUESTÃO 10 - Pode entrar?

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade utilizando um número inteiro: "))

if idade>=12:
    print(f'\n{nome}: Entrada permitida.')

elif idade < 0:
    print ('Idade inválida!')

else:
    print(f'\n{nome}: Entrada NÃO permitida.')