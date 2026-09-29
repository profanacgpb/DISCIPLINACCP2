# Crie numeros.txt, escreva os números de 1 a 20, um por linha, e depois leia e mostre os números.

with open('numeros.txt', 'w') as arquivo:
    for i in range(1, 21):
        arquivo.write(f'{i}\n')

with open('numeros.txt', 'r') as arquivo:
    for numero in arquivo:
        print(f'Número: {numero.strip()}')




