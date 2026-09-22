#Questão 8 — Cadastro de produtos
#Crie um dicionário com 5 produtos e seus preços. Faça: 

lista_produtos = {
    "cafe": 8.50,
    "arroz": 5.35,
    "feijao": 8.95,
    "leite": 4.98,
    "sal": 2.20
}

# a) mostrar todos os produtos; 
print(lista_produtos)

# b) mostrar todos os preços;
print("\nTodos os preços:")  
print(lista_produtos.values())

# c) mostrar produto e preço;
print("\nProduto e preço:") 
print(lista_produtos.items())

#OUTRA FORMA:
print("\nOutra forma para mostrar produto e preço:")
for chave, valor in lista_produtos.items():
    print("O produto",chave, "tem preço:",valor)

# d) mostrar o produto mais caro.

maior_preco = 0
produto_mais_caro = ""

for chave, valor in lista_produtos.items():
    if valor > maior_preco:
        maior_preco = valor
        produto_mais_caro = chave

print("\n")
print(f"O produto mais caro é o {produto_mais_caro} que custa {maior_preco}.")


    