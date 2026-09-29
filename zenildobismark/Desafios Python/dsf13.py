# Transforme o cadastro de alunos das aulas anteriores em funções separadas: 
# cadastrar, listar, buscar e remover.

alunos = []

def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    serie = int(input("Digite a série do aluno: "))
    email = input("Digite o e-mail do aluno: ")
    telefone = int(input("Digite o telefone do aluno: "))

    aluno = {
        'nome': nome,
        'matricula': matricula,
        'serie': serie,
        'email': email,
        'telefone': telefone
    }

    alunos.append(aluno)

def cadastrarNota():
    nome = input("Digete o nome do aluno: ")

    for aluno in alunos:
        if aluno['nome'] == nome:
            if aluno.get['nota1'] is not None and aluno.get['nota2'] is not None and nota1 =! '' and nota2 =! '':
                print("Esse aluno já possui notas cadastradas!")
                return
     
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))

            aluno['nota1'] = nota1
            aluno['nota2'] = nota2

    print("Aluno não encontrado")
    
def alterarNota():

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno['nome'] == nome:
            print('Aluno encontrado!')
            if aluno.get['nota1'] is not None and aluno.get['nota2'] and nota1 =! '' and nota2 =! '':
                print("Digite (1) para alterar a primeira nota")
                print("Digite (2) para alterar a segunda nota")
                print("Digite (3) para alterar as duas notas")

                op = int(input("Digite a opção desejada: "))

                if op == 1:
                    nota1 = float(input('Digite a primeira nova nota: '))
                    aluno['nota1'] = nota1
                elif op == 2:
                    nota2 = float(input('Digite a segunda nova nota: '))
                    aluno['nota2'] = nota2
                else:
                    nota1 = float(input('Digite a primeira nova nota: '))
                    nota2 = float(input('Digite a segunda nova nota: '))
                    aluno['nota1'] = nota1
                    aluno['nota2'] = nota2

        else:
            print("Aluno não encontrado!")
                
def alterarPessoais():
    nome = input("Digite o nome do aluno que você deseja alterar os daods pessoais: ")

    for aluno in alunos:
        if aluno['nome'] == nome:
            while True:
                print("Aluno encontrado!")
                print("Quais dados você deseja alterar?")
                print("Digite (1) para alterar apenas o nome do aluno: ")
                print("Digite (2) para alterar apenas o matricula do aluno: ")
                print("Digite (3) para alterar apenas o serie do aluno: ")
                print("Digite (4) para alterar apenas o email do aluno: ")
                print("Digite (5) para alterar apenas o telefone do aluno: ")
                print("Digite (6) para alterar todos os dados pessoais do aluno: ")
                print("Digite (7) para Sair")

                op = int(input("Digite a opção desejada: "))

                if op == 1:
                    nome = input("Digite o novo nome do aluno: ")
                    aluno['nome'] = nome

                elif op == 2:
                    matricula = int(input("Digite a nova matrícula do aluno: "))
                    aluno['matricula'] = matricula

                elif op == 3:
                    serie = int(input("Digite a mova série do aluno: "))
                    aluno['serie'] = serie

                elif op == 4:
                    

                



def calcularMedia():
    for aluno in alunos:
        nota1 = aluno.get('nota1')
        nota2 = aluno.get('nota2')

        if nota1 is not None and nota2 is not None and nota1 != '' and nota2 != '':
            media = (nota1 + nota2) / 2
            print(aluno['nome'], 'Média:', media)
        else:
            print(aluno['nome'], 'ainda não possui as duas notas.')
