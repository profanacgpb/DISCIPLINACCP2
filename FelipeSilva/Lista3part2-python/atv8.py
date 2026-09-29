arquivo = open("compras.txt", "w")

for i in range(5):
    produto = input("Digite o produto: ")
    arquivo.write(produto + "\n")

arquivo.close()

arquivo = open("compras.txt", "r")

contador = 1

for produto in arquivo:
    print(contador, "-", produto.strip())
    contador += 1

arquivo.close()