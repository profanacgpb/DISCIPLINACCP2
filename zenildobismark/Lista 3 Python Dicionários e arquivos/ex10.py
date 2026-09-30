# Leia o arquivo alunos.txt e imprima todos os nomes na tela.
with open('alunos.txt', 'r') as arquivo:
    for nome in arquivo:
        print(nome.strip())
    