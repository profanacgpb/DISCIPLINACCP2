aluno={
    "Nome":"Pedro Vinicius",
    "Idade": 12,
    "curso":"Ciencia da computação",
    "Cidade": "Campina Grande"
}

print(aluno)

print(aluno["Nome"])

print(aluno["curso"])


#Questão 2

aluno["Idade"] = 20

aluno["curso"] = "Analista de dados"

print(aluno)

#Questão 3

aluno["Email"] = "pedro@gmail.com"

aluno["Telefone"] = 8398899957

print(aluno)

#Questão 4

aluno.pop("Telefone")

print(aluno)

#Questão 5

if "email" in aluno :
    print("E-mail cadastro")
else:
    print("E-mail Não cadastro")
    
#Questão 6

produto = {
    "Nome":"Notebook",
    "Preco": 2500,
    "Marca":"Acer",
    "Estoque" :10
}

for chave, valor in produto.items():
    print(chave, ":", chave)
    

#Questão 7

aluno = {
    "nome": "Sara",
    "nota1": 2,
    "nota2": 3
}

media = (aluno["nota1"] + aluno["nota2"]) /2

print("Aluno", aluno["nome"])
print(media)

if media > 7:
    print("Aprovado")
else:
    print("Reprovado")

#Questão 8

produtos = {
    "Notebook": 2500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Headset": 200
}

# a) Mostrar todos os produtos
print("Produtos:")

for produto in produtos:
    print(produto)


# b) Mostrar todos os preços
print("\nPreços:")

for preco in produtos.values():
    print(preco)


# c) Mostrar produto e preço
print("\nProdutos e preços:")

for produto, preco in produtos.items():
    print(produto, "-", preco)


# d) Mostrar o produto mais caro
produto_mais_caro = max(produtos, key=produtos.get)

print("\nProduto mais caro:")
print(produto_mais_caro, "-", produtos[produto_mais_caro])