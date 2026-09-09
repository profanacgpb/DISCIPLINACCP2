# meu codigo vai começar pedindo os dados de entrada do aluno como nome, idade  e nota.

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
nota = float(input("Digite a nota: "))

# após os dados de entrada o programa irá mostrar os dados de saída que foram armazenados nas variáveis.

print("\n--- DADOS DO ALUNO ---")
print("Nome:", nome)
print("Idade:", idade)
print("Nota:", nota)

# então, logo depois de coletar todos os dados necessários ele vai executar as condições lógicas.

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# fim do programa!