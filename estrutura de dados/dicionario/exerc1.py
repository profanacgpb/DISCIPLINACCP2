# EXERCÍCIOS PRÁTICOS — DICIONÁRIOS

# ==========================================
# QUESTÃO 1 — Cadastro de aluno
# ==========================================

aluno = {
    "nome": "Geovani",
    "idade": 18,
    "curso": "Informática",
    "cidade": "Campina Grande"
}

print("QUESTÃO 1")
print("Dicionário completo:", aluno)
print("Nome:", aluno["nome"])
print("Curso:", aluno["curso"])


# ==========================================
# QUESTÃO 2 — Alteração
# ==========================================

aluno["idade"] = 19
aluno["curso"] = "Programação"

print("\nQUESTÃO 2")
print("Dicionário após as alterações:", aluno)


# ==========================================
# QUESTÃO 3 — Nova informação
# ==========================================

aluno["email"] = "Geovani@email.com"
aluno["telefone"] = "83999999999"

print("\nQUESTÃO 3")
print("Dicionário com novas informações:", aluno)


# ==========================================
# QUESTÃO 4 — Remoção
# ==========================================

del aluno["telefone"]

print("\nQUESTÃO 4")
print("Dicionário após remover o telefone:", aluno)


# ==========================================
# QUESTÃO 5 — Verificação
# ==========================================

print("\nQUESTÃO 5")

if "email" in aluno:
    print("E-mail cadastrado.")
else:
    print("E-mail não cadastrado.")


# ==========================================
# QUESTÃO 6 — Percorrendo o dicionário
# ==========================================

produto = {
    "nome": "Notebook",
    "preco": 2500,
    "marca": "Acer",
    "estoque": 10
}

print("\nQUESTÃO 6")

for chave, valor in produto.items():
    print(chave, ":", valor)


# ==========================================
# QUESTÃO 7 — Sistema de notas
# ==========================================

aluno_notas = {
    "nome": "Geovani",
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


# ==========================================
# QUESTÃO 8 — Cadastro de produtos
# ==========================================

produtos = {
    "Notebook": 2500,
    "Celular": 1500,
    "Tablet": 1200,
    "Fone": 200,
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
mais_caro = max(produtos, key=produtos.get)

print("\nProduto mais caro:")
print(mais_caro, ":", produtos[mais_caro])