nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade >= 12:
    print(f'{nome} entrada permitida')
else:
    print(f'{nome} entrada não permitida')