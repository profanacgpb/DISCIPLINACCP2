arquivo = open("notas.txt", "w")

arquivo.write("Ana;8.5\n")
arquivo.write("Carlos;7.0\n")
arquivo.write("Joao;9.2\n")
arquivo.write("Maria;6.8\n")
arquivo.write("Pedro;8.0\n")

arquivo.close()

arquivo = open("notas.txt", "r")

for linha in arquivo:
    dados = linha.strip().split(";")

    nome = dados[0]
    nota = dados[1]

    print("Aluno:", nome, "- Nota:", nota)

arquivo.close()