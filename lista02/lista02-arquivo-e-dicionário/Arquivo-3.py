#Questão 9-  Notas dos alunos
nome= input("Digite seu nome: ")
nota= float(input("Digite sua nota: "))
with open ("notas", "w")as notas:
    notas.write(nome+";")
    notas.write(str(nota))