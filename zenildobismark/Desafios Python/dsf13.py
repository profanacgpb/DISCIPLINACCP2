# Transforme o cadastro de alunos das aulas anteriores em funções separadas: 
# cadastrar, listar, buscar e remover.

alunos = []

def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    serie = int(input("Digite a série do aluno: "))

    aluno = {
        'nome': nome,
        'serie': serie
    }

    alunos.append(aluno)

def cadastrarNota():
    nome = input("Digete o nome do aluno: ")

    for aluno in alunos:
        if aluno['nome'] == nome:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))

        aluno['nota1'] = nota1
        aluno['nota2'] = nota2
    
    print("Aluno não encontrado! ")

def calcularMedia():
    for aluno in alunos:
        nota1 = aluno.get('nota1')
        nota2 = aluno.get('nota2')


