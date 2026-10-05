# Questão 1

pessoa = {
    "nome": "Daniel",
    "idade": 18,
    "cidade": "Campina Grande"
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])


# Questão 2

agenda = {
    "Maria": ("(11) 9999-9999", "maria@email.com"),
    "Joao": ("(83) 9888-8888", "joao@email.com"),
    "Ana": ("(83) 9777-7777", "ana@email.com")
}

for nome in agenda:
    print(nome, "-> Telefone:", agenda[nome][0], "| Email:", agenda[nome][1])


# Questão 3

cidades = {
    (-23.55, -46.63): "São Paulo",
    (-8.05, -34.90): "Recife",
    (-7.23, -35.88): "Campina Grande"
}

coordenada = (-7.23, -35.88)

print(cidades[coordenada])


# Questão 4

alunos = {
    "Ana": (8, 7, 9),
    "Joao": (6, 8, 7),
    "Maria": (9, 10, 8)
}

nome = input("Digite o nome do aluno: ")

if nome in alunos:
    print("Notas:", alunos[nome])

for aluno in alunos:
    notas = alunos[aluno]
    media = (notas[0] + notas[1] + notas[2]) / 3
    print(aluno, "- Média:", media)


# Questão 5

precos = {
    ("Camiseta", "P"): 30,
    ("Camiseta", "M"): 35,
    ("Camiseta", "G"): 40,
    ("Calca", "P"): 50,
    ("Calca", "M"): 55,
    ("Calca", "G"): 60
}

produto = input("Digite o produto: ")
tamanho = input("Digite o tamanho: ")

chave = (produto, tamanho)

if chave in precos:
    print("Preço:", precos[chave])
else:
    print("Produto não encontrado")


# Questão 6

tabuleiro = {
    (0, 0): "X", (0, 1): "-", (0, 2): "O",
    (1, 0): "-", (1, 1): "X", (1, 2): "-",
    (2, 0): "O", (2, 1): "-", (2, 2): "X"
}

for linha in range(3):
    for coluna in range(3):
        print(tabuleiro[(linha, coluna)], end=" ")
    print()


# Questão 7

notas = {
    ("Ana", "Matemática"): 9,
    ("Ana", "História"): 7,
    ("Ana", "Português"): 8,
    ("Joao", "Matemática"): 6,
    ("Joao", "História"): 8,
    ("Joao", "Português"): 7
}

nome = input("Digite o nome do aluno: ")

soma = 0
quantidade = 0

for chave in notas:
    if chave[0] == nome:
        print(chave[1], "-", notas[chave])
        soma = soma + notas[chave]
        quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
else:
    print("Aluno não encontrado")


# Questão 8

pontos_turisticos = {
    (-22.95, -43.21): "Cristo Redentor",
    (-12.97, -38.51): "Elevador Lacerda",
    (-7.22, -35.88): "Açude Velho"
}

latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

coordenada = (latitude, longitude)

if coordenada in pontos_turisticos:
    print(pontos_turisticos[coordenada])
else:
    print("Não existe ponto turístico cadastrado nesse local")


# Desafio Final

alunos = {}

opcao = 0

while opcao != 4:
    print("1 - Cadastrar aluno")
    print("2 - Consultar notas")
    print("3 - Calcular média")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Nome do aluno: ")
        disciplina = input("Disciplina: ")

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        alunos[(nome, disciplina)] = (nota1, nota2, nota3)

        print("Aluno cadastrado")

    elif opcao == 2:
        nome = input("Nome do aluno: ")

        encontrou = False

        for chave in alunos:
            if chave[0] == nome:
                print("Disciplina:", chave[1])
                print("Notas:", alunos[chave])
                encontrou = True

        if encontrou == False:
            print("Aluno não encontrado")

    elif opcao == 3:
        nome = input("Nome do aluno: ")

        soma = 0
        quantidade = 0

        for chave in alunos:
            if chave[0] == nome:
                notas = alunos[chave]

                soma = soma + notas[0]
                soma = soma + notas[1]
                soma = soma + notas[2]

                quantidade = quantidade + 3

        if quantidade > 0:
            media = soma / quantidade
            print("Média geral:", media)
        else:
            print("Aluno não encontrado")

    elif opcao == 4:
        print("Programa encerrado")

    else:
        print("Opção inválida")