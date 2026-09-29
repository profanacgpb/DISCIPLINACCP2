# Crie um programa que permita ao usuário cadastrar nomes. 
# Os nomes devem ser armazenados no arquivo alunos.txt.

alunos = []

while True:
    print("Digite (1) para adicionar um aluno:")
    print("Digite (2) para SAIR")

    op = int(input("Digite a opção desejada: "))

    if op == 1:
        aluno = input("Digite o nome do aluno: ")
        alunos.append(aluno)

    elif op == 2:
        print("Sistema encerrado")
        break

with open('alunos.txt', 'a') as arquivo:
    for aluno in alunos:
        arquivo.write(f'Aluno: {aluno}\n')