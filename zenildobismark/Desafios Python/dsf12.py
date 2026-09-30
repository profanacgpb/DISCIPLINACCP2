# Crie uma lista de dicionários representando alunos e calcule a média de cada um.

alunos = [
    {"nome": "João", "nota1": 7.5, "nota2": 8.0},
    {"nome": "Maria", "nota1": 9.0, "nota2": 8.5},
    {"nome": "Pedro", "nota1": 6.0, "nota2": 7.0},
    {"nome": "Ana", "nota1": 8.5, "nota2": 9.0},
    {"nome": "Carlos", "nota1": 5.5, "nota2": 6.5},
    {"nome": "Juliana", "nota1": 10.0, "nota2": 9.5},
    {"nome": "Lucas", "nota1": 7.0, "nota2": 6.5},
    {"nome": "Rafael", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Fernanda", "nota1": 9.5, "nota2": 9.0},
    {"nome": "Gabriel", "nota1": 6.5, "nota2": 7.5}
]

for aluno in alunos:
    print(f"Aluno: {aluno['nome']} || Média: {(aluno['nota1'] + aluno['nota2']) / 2}")