nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))

if idade >= 18 and nota >= 7:
    print(f"Olá {nome}, você é maior de idade e foi aprovado!")

else:
    print(f"Olá {nome}, você não atende aos critérios de aprovação.")