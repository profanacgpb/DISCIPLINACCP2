nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))

if idade  >=18:
    print("Situação: Você é maior de idade")
else: 
    print("Situação: Você é menor de idade")
if nota >=7:
    print("Resultado: Aprovado")
else:
    print("Resultado: reprovado")