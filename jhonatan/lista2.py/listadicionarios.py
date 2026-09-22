"""
Soluções — Exercícios práticos de Dicionários
Material: Estrutura de Dados / Introdução à programação em Python
"""


# Questão 1 — Cadastro de aluno

print("=== Questão 1 ===")

aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "ADS",
    "cidade": "Campina Grande"
}

# a)
print(aluno)

# b)
print(aluno["nome"])

# c)
print(aluno["curso"])


# Questão 2 — Alteração

print("\n=== Questão 2 ===")

# a)
aluno["idade"] = 21

# b)
aluno["curso"] = "Computação"

# c)
print(aluno)



# Questão 3 — Nova informação

print("\n=== Questão 3 ===")

aluno["email"] = "ana@email.com"
aluno["telefone"] = "83999999999"

print(aluno)



# Questão 4 — Remoção

print("\n=== Questão 4 ===")

aluno.pop("telefone")
print(aluno)


# Questão 5 — Verificação
print("\n=== Questão 5 ===")

if "email" in aluno:
    print("E-mail cadastrado.")
else:
    print("E-mail não cadastrado.")

# Questão 6 — Percorrendo o dicionário

print("\n=== Questão 6 ===")

produto = {
    "nome": "Notebook",
    "preco": 2500,
    "marca": "Acer",
    "estoque": 10
}

for chave, valor in produto.items():
    print(chave, "→", valor)



# Questão 7 — Sistema de nota
print("\n=== Questão 7 ===")

aluno_nota = {
    "nome": "João",
    "nota1": 8,
    "nota2": 6
}

media = (aluno_nota["nota1"] + aluno_nota["nota2"]) / 2
print("Média:", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")



# Questão 8 — Cadastro de produtos
print("\n=== Questão 8 ===")

produtos = {
    "Notebook": 2500,
    "Mouse": 50,
    "Teclado": 100,
    "Monitor": 800,
    "Headset": 150
}

# a)
print("Produtos:")
for nome_produto in produtos.keys():
    print("-", nome_produto)

# b)
print("\nPreços:")
for preco in produtos.values():
    print("-", preco)

# c)
print("\nProduto e preço:")
for nome_produto, preco in produtos.items():
    print(nome_produto, "→", preco)

# d)
produto_mais_caro = max(produtos, key=produtos.get)
print("\nProduto mais caro:", produto_mais_caro, "-", produtos[produto_mais_caro])