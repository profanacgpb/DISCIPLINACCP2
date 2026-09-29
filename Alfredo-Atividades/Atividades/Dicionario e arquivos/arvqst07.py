with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        arquivo.write(nome + "\n")
        print(f"Aluno '{nome}' cadastrado com sucesso!")

print("Cadastro finalizado. Os nomes foram salvos em alunos.txt")