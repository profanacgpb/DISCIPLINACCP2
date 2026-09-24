#Questão 9 - Notas dos alunos
with open("notas.txt", "w") as arquivo:
    alunos = {
        "Ana": 8.5,
        "Daniel": 9.0,
        "Gabriel": 8.0
    }
    for aluno, nota in alunos.items():
        arquivo.write(f"O aluno {aluno} obteve a nota {nota}!\n")