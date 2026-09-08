#coleta de informações do aluno
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))

#nome e idade do aluno

print("Nome:", nome)
print("Idade:", idade)

#informação sobre a situação do aluno

if idade >= 18:
    print("Situação: maior de idade.")
else:
    print("Situação: menor de idade.")

if nota >= 7.0:
    print("Resultado: Aprovado.")
else:
    print("Resultado: Reprovado.")