# EXERCÍCIOS PRÁTICOS — DICIONÁRIOS


# QUESTÃO 1 — Cadastro de aluno

aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Ciência da Computação",
    "cidade": "Campina Grande"
}

print("QUESTÃO 1")
print(aluno)
print(aluno["nome"])
print(aluno["curso"])


# QUESTÃO 2 — Alteração

aluno["idade"] = 21
aluno["curso"] = "Engenharia de Software"

print("\nQUESTÃO 2")
print(aluno)


# QUESTÃO 3 — Nova informação

aluno["email"] = "maria@email.com"
aluno["telefone"] = "83999999999"

print("\nQUESTÃO 3")
print(aluno)


# QUESTÃO 4 — Remoção

del aluno["telefone"]

print("\nQUESTÃO 4")
print(aluno)


# QUESTÃO 5 — Verificação

print("\nQUESTÃO 5")

if "email" in aluno:
    print("E-mail cadastrado.")
else:
    print("E-mail não cadastrado.")


# QUESTÃO 6 — Percorrendo o dicionário

produto = {
    "nome": "Notebook",
    "preco": 2500,
    "marca": "Acer",
    "estoque": 10
}

print("\nQUESTÃO 6")

for chave, valor in produto.items():
    print(chave, ":", valor)


# QUESTÃO 7 — Sistema de notas

aluno_notas = {
    "nome": "João",
    "nota1": 8,
    "nota2": 6
}

media = (aluno_notas["nota1"] + aluno_notas["nota2"]) / 2

print("\nQUESTÃO 7")
print("Aluno:", aluno_notas["nome"])
print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# QUESTÃO 8 — Cadastro de produtos

produtos = {
    "Notebook": 2500,
    "Celular": 1800,
    "Tablet": 1200,
    "Teclado": 150,
    "Monitor": 900
}

print("\nQUESTÃO 8")

# a) Mostrar todos os produtos
print("\nTodos os produtos:")
for produto in produtos:
    print(produto)

# b) Mostrar todos os preços
print("\nTodos os preços:")
for preco in produtos.values():
    print(preco)

# c) Mostrar produto e preço
print("\nProduto e preço:")
for produto, preco in produtos.items():
    print(produto, ":", preco)

# d) Mostrar o produto mais caro
produto_mais_caro = max(produtos, key=produtos.get)

print("\nProduto mais caro:")
print(produto_mais_caro, ":", produtos[produto_mais_caro])