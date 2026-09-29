# Crie um programa que permita cadastrar 5 produtos em compras.txt. 
# Depois leia o arquivo e apresente os produtos numerados.

compras = []

while True:
    print("Digite (1) para adicionar PRODUTOS: ")
    print("Digite (2) para SAIR")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        produto = input("Digite o nome do produto: ")
        compras.append(produto)
        print('Produto adicionado com sucesso: ')

    elif op == 2:
        print("Programa encerrado!")
        break

with open('compras.txt', 'w') as arquivo:
    contador = 1
    for compra in compras:
        arquivo.write(f'Produto {contador}: {compra}\n')
        contador += 1

with open('compras.txt', 'r') as arquivo:
    produto = arquivo.read()
    print(produto.strip())