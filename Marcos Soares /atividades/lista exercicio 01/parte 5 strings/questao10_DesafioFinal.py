nome = input("qual é o seu nome? ")
idade = int(input("qual é sua idade "))
nota1 = int(input("qual a sua primeira nota? "))
nota2 = int(input("qual a sua segunda nota? "))
media = (nota1 + nota2) / 2
if idade < 18:
    print("menor de idade")
else:
    print("maior de idade")

if media >= 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")