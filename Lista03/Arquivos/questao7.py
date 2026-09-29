#Questão 7 - Cadastro de alunos
with open("alunos.txt", "w") as alunos:
    for cad in range(1,5):
        with open("alunos.txt" , "a") as alunos2:
            cadastro = input("Digite o usuário que você quer cadastrar: ")
            alunos.write(f"Nome:{cadastro}\n")