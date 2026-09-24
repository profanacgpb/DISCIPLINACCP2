#  Notas dos alunos

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/compras.txt", "w")

quantidade_cadastro_aluno = int(input("Digite a quantidade de aluno que quer cadastrar: "))

if quantidade_cadastro_aluno > 0:
    for indice in range (1, quantidade_cadastro_aluno+1, +1):
        name_student = str(input(f"Digite o nome do aluno ({indice}): "))
        grade_student = str(input(f"Digite sua media escolar ({indice}): "))
        arquivo.write (f"{name_student}:{grade_student}" + "\n")
else:
    print (f"Verifique a quantidade, você digitou: {quantidade_cadastro_aluno}")
arquivo.close()

arquivo = open ("Gabriel-Porto/Python-Estrutura-de-Dados/Arquivos/Questão-01-a-10/compras.txt", "r")
print ("\n")
exibicao_aluno = arquivo.read()
print (exibicao_aluno)

arquivo.close()