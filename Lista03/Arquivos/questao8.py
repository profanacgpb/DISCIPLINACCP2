#Questão 8 - Lista de compras
with open("compras.txt", "w") as arquivo:
    for cad in range(0,5):
        with open("compras.txt", "a") as arquivo2:
            cadastro = input("Digite o produto que você deseja cadastrar: ")
            arquivo.write(f"{cad+1} - {cadastro}\n")

with open("compras.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)