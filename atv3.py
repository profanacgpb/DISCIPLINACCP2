# SISTEMA DE CADASTRO

cadastros = []

# Cadastro 1
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")

aluno = {
    "Nome": nome,
    "Idade": idade,
    "Curso": curso
}

cadastros.append(aluno)

# Cadastro de outros alunos
while True:
    continuar = input("\nDeseja cadastrar outra pessoa? (s/n): ")

    if continuar.lower() != "s":
        break

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Curso": curso
    }

    cadastros.append(aluno)

# Mostra os cadastros
print("\n--- CADASTROS ---")

for aluno in cadastros:
    print("Nome:", aluno["Nome"])
    print("Idade:", aluno["Idade"])
    print("Curso:", aluno["Curso"])
    print("----------------")

# Salva os dados em um arquivo
with open("cadastros.txt", "w", encoding="utf-8") as arquivo:
    for aluno in cadastros:
        arquivo.write("Nome: " + aluno["Nome"] + "\n")
        arquivo.write("Idade: " + str(aluno["Idade"]) + "\n")
        arquivo.write("Curso: " + aluno["Curso"] + "\n")
        arquivo.write("----------------\n")

print("Cadastros salvos em cadastros.txt")