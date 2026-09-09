# Desafio 4 — Lista de dicionários 
# Agora vamos trabalhar com uma estrutura mais próxima de aplicações reais. 
# Crie: alunos = [ {"nome": "Ana", "nota": 8.5}, 
#                   {"nome": "Carlos", "nota": 7.0}, 
#                   {"nome": "Maria", "nota": 9.2}, 
#                   {"nome": "João", "nota": 6.5} ] 
# Percorra a estrutura: 
# for aluno in alunos: 
#   print(aluno["nome"], aluno["nota"]) 
# Resultado: Ana 8.5 Carlos 7.0 Maria 9.2 João 6.5


alunos = [ 
            {"nome": "Ana", "nota": 8.5}, 
            {"nome": "Carlos", "nota": 7.0}, 
            {"nome": "Maria", "nota": 9.2}, 
            {"nome": "João", "nota": 6.5} 
        ]

for aluno in alunos:
    print(aluno['nome'], aluno['nota'])