arquivo = open("compras.txt", "w")

for i in range(5):
    produto = input("Digite o produto: ")
    arquivo.write(produto + "\n")

arquivo.close()