arquivo = open("notas.txt", "w")

arquivo.write("Ana;8.5\n")
arquivo.write("Bruno;7.0\n")
arquivo.write("Carlos;9.5\n")
arquivo.write("Daniela;6.5\n")

arquivo.close()

arquivo = open("notas.txt", "r")

for linha in arquivo:
    dados = linha.strip().split(";")

    nome = dados[0]
    nota = dados[1]

    print("Aluno:", nome)
    print("Nota:", nota)

arquivo.close()