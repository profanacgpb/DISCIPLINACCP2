# Cadastro de alunos

quantidade_cadastro = int(input("Quantos alunos você quer cadastrar (?): "))

if quantidade_cadastro > 0:
    arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/alunos-cadastro.txt", "w")
    for indice in range (1, quantidade_cadastro+1, +1):
        nome_aluno = input(f"Digite o nome do aluno ({indice}): ")
        arquivo.write (nome_aluno + "\n")
else:
    print (f"Por favor verifique o número digitado e tente novamente, você digitou {quantidade_cadastro}")

arquivo.close()
