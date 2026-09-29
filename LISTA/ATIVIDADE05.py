#1- Crie uma função chamada apresentar() que exiba a mensagem abaixo. Depois, chame a função.
nome = input("Digite o seu nome: ")
def apresentar(nome):
    print(f"{nome}! Bem-vindo à disciplina de Programação!")
apresentar(nome)
#2- Crie uma função saudacao(nome) que receba um nome e exiba uma saudação.
nome2 = input("Digite o seu nome: ")
def saudacao(nome2):
    print(f"Saudação {nome2}!")
saudacao(nome2)
#3- Crie somar(a, b) e faça a função retornar a soma. Teste com 15 e 25.
def somar(a, b):
    return a + b
resultado = somar(15, 25)
print(resultado)
#4- Crie calcular_media(n1, n2, n3) e retorne a média das três notas.
n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))
n3 = float(input("Digite o numero 3: "))
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
result = calcular_media(n1, n2, n3)
print(result)
#5- Crie verificar_par(numero). A função deve retornar True se o número for par e False caso contrário.
numero = int(input("Digite um numero: "))
def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
resultado = verificar_par(numero)
print(resultado)
#6- Crie maior(a, b) para retornar o maior de dois números. Não utilize max().
a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
def maior(a, b):
    if a > b:
        return "1 numero é maior que o segundo"
    elif b > a:
        return "2 numero é maior que o primeiro"
resultado = maior(a, b)
print(resultado)
#7- Crie quatro funções: somar(), subtrair(), multiplicar() e dividir(). Depois crie um programa principal para escolher a operação.
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def main_calculadora():
    print("--- CALCULADORA ---")
    print("1. Somar | 2. Subtrair | 3. Multiplicar | 4. Dividir")

    opcao = input("Escolha a operação (1-4): ")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print(f"Resultado: {somar(n1, n2)}")
    elif opcao == "2":
        print(f"Resultado: {subtrair(n1, n2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicar(n1, n2)}")
    elif opcao == "4":
        print(f"Resultado: {dividir(n1, n2)}")
    else:
        print("Opção inválida!")
#8- Desenvolva um programa com as funções ler_notas(), calcular_media(), verificar_situacao() e exibir_resultado().
def ler_notas():
    notas = []
    for i in range(1, 3):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)
    return notas
def calcular_media(notas):
    return sum(notas) / len(notas)
def verificar_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Em Recuperação"
    else:
        return "Reprovado"
def exibir_resultado(media, situacao):
    print(f"\nMédia final: {media:.2f}")
    print(f"Situação: {situacao}")
def main_notas():
    print("--- SISTEMA DE NOTAS ---")
    notas = ler_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_resultado(media, situacao)
#9- Crie funções cadastrar_aluno(), listar_alunos() e buscar_aluno(). Utilize listas ou dicionários para armazenar os dados.
# Lista global para armazenar os dicionários dos alunos
alunos = []
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    curso = input("Digite o curso do aluno: ")

    aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!\n")
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    print("\n--- LISTA DE ALUNOS ---")
    for i, aluno in enumerate(alunos, 1):
        print(
            f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}"
        )
    print("-" * 25 + "\n")
def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ").lower()
    encontrados = [a for a in alunos if nome_busca in a["nome"].lower()]
    if not encontrados:
        print("Nenhum aluno encontrado com esse nome.\n")
        return
    print("\n--- RESULTADO DA BUSCA ---")
    for aluno in encontrados:
        print(
            f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}"
        )
    print("-" * 26 + "\n")
def main_cadastro():
    while True:
        print("--- CADASTRO DE ALUNOS ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Buscar Aluno")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")
