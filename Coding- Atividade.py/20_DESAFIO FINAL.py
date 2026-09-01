nome= input("digite seu nome ")
idade= int(input("digite sua idade "))
nota= float(input("digite sua nota "))
print("Nome:", nome)
print("Idade:", idade)
if idade>=18:
    print("maior de idade")
else:
    print("menor de idade")
if nota>=7:
    print("aprovado")
else:
    print("reprovado")