caminho = r"C:\Users\4lfr3\DISCIPLINACCP2\Alfredo-Atividades\alunos.txt"  #para poder ler o arquivo na minha pasta, para ficar organizado

with open(caminho, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)              