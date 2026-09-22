with open("mensagem.txt", "w") as arquivo:
    arquivo.write("Primeira mensagem")

with open("mensagem.txt", "w") as arquivo:
    arquivo.write("Nova mensagem")

with open("mensagem.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
