mensagem = r"C:\Users\4lfr3\DISCIPLINACCP2\Alfredo-Atividades\mensagem.txt"

with open(mensagem, "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira mensagem")

with open(mensagem, "w", encoding="utf-8") as arquivo:
    arquivo.write("Nova mensagem")

with open(mensagem, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)