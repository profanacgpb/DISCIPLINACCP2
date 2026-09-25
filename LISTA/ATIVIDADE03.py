#1- Cadastro de aluno
aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Engenharia",
    "cidade": "Campina Grande"
}
print("a) Dicionário completo:", aluno)
print("b) Apenas o nome:", aluno["nome"])
print("c) Apenas o curso:", aluno["curso"])
#2- Alteração
aluno["idade"] = 21
aluno["curso"] = "Ciência da Computação"
print("Dicionário alterado:", aluno)
#3- Nova informação
aluno["email"] = "ana@email.com"
aluno["telefone"] = "83-99999-9999"
print("Com novas informações:", aluno)
#4- Remoção
aluno.pop("telefone")
print("Após remover o telefone:", aluno)
#5- Verificação
if "email" in aluno:
    print("E-mail cadastrado.")
else:
    print("E-mail não cadastrado.")
#6- Percorrendo o dicionário
produto = {"nome": "Notebook", "preco": 2500, "marca": "Acer", "estoque": 10}
for chave, valor in produto.items():
    print(f"{chave}: {valor}")
#7- Sistema de notas
aluno_notas = {"nome": "João", "nota1": 8, "nota2": 6}
media = (aluno_notas["nota1"] + aluno_notas["nota2"]) / 2
print(f"Média do {aluno_notas['nome']}: {media}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
#8- Cadastro de produtos
produtos = {
    "Mouse": 50.0,
    "Teclado": 120.0,
    "Monitor": 800.0,
    "Cadeira": 1200.0,
    "Mesa": 450.0
}
print("Todos os produtos:", list(produtos.keys()))
print("Todos os preços:", list(produtos.values()))
print("Produto e preço:")
for prod, preco in produtos.items():
    print(f"   {prod} -> R$ {preco}")

produto_mais_caro = max(produtos, key=produtos.get)
print(f"Produto mais caro: {produto_mais_caro} (R$ {produtos[produto_mais_caro]})")
