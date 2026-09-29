# Lista de compras

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/compras.txt", "w")

for indice in range (1, 6, +1):
    nome_produto = input (f"Digite o nome do produto ({indice}): ")
    arquivo.write (nome_produto + "\n")

arquivo.close()

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/compras.txt", "r")
print ("\n")
produtos = arquivo.read()
print (produtos)

arquivo.close()