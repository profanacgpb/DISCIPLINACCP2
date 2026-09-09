#Crie um perfil de aluno com nome, matrícula, curso, idade e média. Exiba os dados de forma organizada.

nome = input("Digite seu nome: ")
matricula = int(input("Digite sua matrícula: "))
curso = input("Digite seu curso: ")
idade = int(input("Digite sua idade: "))
media = float(input("Digite sua média: "))

print(f"Nome: {nome} || {type(nome)}")
print(f"Matrícula: {matricula} || {type(matricula)}")
print(f"Curso: {curso} || {type(curso)}")
print(f"Idade: {idade} || {type(idade)}")
print(f"Média: {media} || {type(media)}")
