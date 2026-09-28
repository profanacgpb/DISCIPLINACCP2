#Questão 1//2//3 —Primeiro arquivo, Leitura, Linha por linha
with open("dados", "w")as arquivo:
   arquivo.write("Aluno: Pedro\n")
   arquivo.write("Aluno: Enzo\n")
   arquivo.write("Aluno: Kleyton\n")
   arquivo.write("Aluno: Henrique\n")
   arquivo.write("Aluno: Josemir\n")
with open("dados", "r") as arquivo:
   print(arquivo.read())

#Questão 4-Números
with open("Numeros", "w")as numeros:
   for i in range(1, 21):
        numeros.write(f"{i}\n")
with open("Numeros", "r")as Numeros:
   print(Numeros.read())
#Questão 5-Append
with open("Numeros", "a")as numeros:
 for i in range(22, 31):
    numeros.write(f"{i}\n")
with open("Numeros", "r")as Numeros:    
    print(Numeros.read())

#Questão 6- Substituição
with open("Mensage", "w")as Mensage:
   Mensage.write("Primeira Mensagem")
with open("Mensage", "r")as Mensage:
   conteudo= Mensage.read()
   print(conteudo)
conteudo= conteudo.replace("Primeira Mensagem", "Outra mensagem")
with open("Mensage", "w")as Mensage:
   Mensage.write(conteudo)
with open("Mensage", "r")as mensage:
    print(conteudo)  

#Questão 7-Cadastro de alunos
nome= input("Digite seu nome: ")
with open("Cadastro", "w")as Cadastro:
   Cadastro.write(nome)

