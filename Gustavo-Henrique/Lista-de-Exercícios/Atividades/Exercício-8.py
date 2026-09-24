# Número positivo ou negativo

n = int(input('Digite um número inteiro: '))
if n < 0:
    print(f'Este número é negativo')
elif n > 0:
    print(f'Este é um número positivo')
else:
    print('Este é um número neutro')