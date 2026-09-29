with open("notas.txt", "w") as arquivo:
    arquivo.write("Ana;8.5\n")
    arquivo.write("Carlos;7.0\n")
    arquivo.write("Maria;9.0\n")

with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")
        nome = dados[0]
        nota = dados[1]
        print("Aluno:", nome)
        print("Nota:", nota)
