arquivo = open("notas.txt", "w")

arquivo.write("Ana;8.5\n")
arquivo.write("Carlos;7.0\n")
arquivo.write("Maria;9.5\n")
arquivo.write("Felipe;10.0\n")

arquivo.close()

arquivo = open("notas.txt", "r")

for linha in arquivo:
    nome, nota = linha.strip().split(";")

    print("Aluno:", nome)
    print("Nota:", nota)

arquivo.close()