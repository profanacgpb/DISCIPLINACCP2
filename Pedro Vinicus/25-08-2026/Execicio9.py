numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
if numero1 > numero2:
    print(f'O numero {numero1} é maior que o numero {numero2}')
elif numero2 > numero1:
    print(f'O numero {numero2} é maior que o numero {numero1}')
else:
    print('Os numeros são iguais')