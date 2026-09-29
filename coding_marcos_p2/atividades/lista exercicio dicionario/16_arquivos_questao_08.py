with open("compras.txt", "w") as arquivo:
    for i in range(5):
        produto = input("Digite um produto: ")
        arquivo.write(produto + "\n")

with open("compras.txt", "r") as arquivo:
    numero = 1
    for linha in arquivo:
        print(numero, "-", linha.strip())
        numero += 1
