alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Maria", "nota": 9.2},
    {"nome": "João", "nota": 6.5}
]

print("Lista de alunos e notas:\n")

for aluno in alunos:
    print(f"{aluno['nome']} = {aluno['nota']}")