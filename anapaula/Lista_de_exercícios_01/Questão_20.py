#QUESTÃO 20 - Desafio Final (PRIMEIRA FORMA)

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
nota = float(input('Digite sua nota: '))
print('\n')

print (f'Nome: {nome}')
print (f'Idade: {idade}')

if idade >= 18:
    print ('Situação: MAIOR de idade.')
else:
    print ('Situação: MENOR de idade.')


if nota>=7:
    print ('Resultado: Aprovado.')
else:
    print('Resultado: Reprovado.')



#QUESTÃO 20 - Desafio Final (SEGUNDA FORMA)
#Pensei nesta forma enquanto digitava a primeira e resolvi colocar também.

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
nota = float(input('Digite sua nota: '))

if idade >= 18:
    s = 'MAIOR de idade.'
else:
    s = 'MENOR de idade.'

if nota>=7:
    r = 'Aprovado.'
else:
    r = 'Reprovado.'

print('\n')
print (f'Nome: {nome}')
print (f'Idade: {idade}')
print (f'Situação: {s}')
print (f'Resultado: {r}')