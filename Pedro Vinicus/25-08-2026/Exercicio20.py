nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
nota = float(input('Digite a sua nota: '))

if nota >= 7:
    print(f'{nome} aprovado')
else:
    print(f'{nome} reprovado')
    
if idade >= 18:
    print(f'{nome} é maior de idade')
else:
    print(f'{nome} é menor de idade')