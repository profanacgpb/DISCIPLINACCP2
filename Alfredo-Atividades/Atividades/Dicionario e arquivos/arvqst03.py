caminho = r"C:\Users\4lfr3\DISCIPLINACCP2\Alfredo-Atividades\alunos.txt"

with open(caminho, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome = linha.strip()
        print(f"Aluno: {nome}")