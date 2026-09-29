# Leia o arquivo alunos.txt e apresente os nomes um por vez, por exemplo: Aluno: Ana.
with open('alunos.txt', 'r') as arquivo:
    for nome in arquivo:
        print(f'Nome: {nome.strip()}')