alunos = []

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
curso = input("Digite o curso: ")

aluno = {
    "nome": nome,
    "idade": idade,
    "curso": curso
}

alunos.append(aluno)

with open("alunos.txt", "a") as arquivo:
    for aluno in alunos:
        arquivo.write(
            aluno["nome"] + ";" +
            aluno["idade"] + ";" +
            aluno["curso"] + "\n"
        )

print("Aluno cadastrado com sucesso!")