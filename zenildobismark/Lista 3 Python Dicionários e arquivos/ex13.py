# Utilizando o arquivo da questão anterior: 
# a) adicione os números de 21 a 30;
with open ('numeros.txt', 'a') as arquivo:
    for i in range(21, 31):
        arquivo.write(f'{i}\n')

with open('numeros.txt', 'r') as arquivo:
    for numero in arquivo:
        print(f'Número: {numero.strip()}')