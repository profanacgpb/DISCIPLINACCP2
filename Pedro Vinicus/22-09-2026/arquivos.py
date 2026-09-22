arquivo = open("alunos.txt", "w") 
arquivo.write("Ana\n") 
arquivo.write("João\n") 
arquivo.write("Pedro\n") 
arquivo.write("Maria\n") 
arquivo.write("Carlos\n") 
arquivo.close()

#Questão 2

arquivo = open("alunos.txt", "r") 
conteudo = arquivo.read() 
print(conteudo) 
arquivo.close()

#Questão 3

arquivo = open("alunos.txt", "r") 
for nome in arquivo: print("Aluno:", nome.strip()) 
arquivo.close()


#Questão 4

arquivo = open("numeros.txt", "w") 
for numero in range(1, 21): arquivo.write(str(numero) + "\n") 
arquivo.close() 
arquivo = open("numeros.txt", "r") 
for numero in arquivo: print(numero.strip()) 
arquivo.close()

#Questão 5

arquivo = open("numeros.txt", "a") 
for numero in range(21, 31): arquivo.write(str(numero) + "\n") 
arquivo.close() 
arquivo = open("numeros.txt", "r") 
for numero in arquivo: print(numero.strip()) 
arquivo.close()

#Questão 6

arquivo = open("mensagem.txt", "w") 
arquivo.write("Primeira mensagem") 
arquivo.close() 
arquivo = open("mensagem.txt", "w") 
arquivo.write("Nova mensagem") 
arquivo.close() 
arquivo = open("mensagem.txt", "r") 
print(arquivo.read())
arquivo.close()

#Questão 7

nome = input("Digite o nome do aluno: ")
arquivo = open("alunos.txt", "a") 
arquivo.write(nome + "\n") 
arquivo.close() 
print("Aluno cadastrado com sucesso!")

#Questão 8

arquivo = open("compras.txt", "w")
for i in range(5): produto = input("Digite um produto: ") 
arquivo.write(produto + "\n") 
arquivo.close() 
arquivo = open("compras.txt", "r") 
contador = 1 
for produto in arquivo: print(contador, "-", produto.strip()) 
contador += 1 
print(contador, "-", produto.strip()) 
contador += 1 
arquivo.close()

#Questão 9
arquivo = open("notas.txt", "w") 
arquivo.write("Ana;8.5\n") 
arquivo.write("João;7.0\n") 
arquivo.write("Pedro;9.0\n") 
arquivo.write("Maria;6.5\n") 
arquivo.close()

arquivo = open("notas.txt", "r") 
for linha in arquivo: nome, nota = linha.strip().split(";") 
print("Aluno:", nome) 
print("Nota:", nota) 
print() 
arquivo.close()

#Questão 10

while True:

    print("\n--- SISTEMA DE ALUNOS ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome do aluno: ")

        arquivo = open("alunos.txt", "a")

        arquivo.write(nome + "\n")

        arquivo.close()

        print("Aluno cadastrado com sucesso!")


    elif opcao == "2":

        arquivo = open("alunos.txt", "r")

        print("\n--- ALUNOS CADASTRADOS ---")

        for aluno in arquivo:
            print(aluno.strip())

        arquivo.close()


    elif opcao == "3":

        print("Programa encerrado.")

        break


    else:

        print("Opção inválida!")