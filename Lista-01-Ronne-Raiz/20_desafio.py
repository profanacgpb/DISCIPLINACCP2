nome = input("isira seu nome ")
idade = int(input("sua idade "))
nota =  float(input("sua nota "))

print(f"seu nome é {nome}")
if idade >= 18:
 print(f"sua idade é {idade} você é maior de idade")
else:
 print("menor de idade ")
if nota >=7:
 print("aprovado")
else:
 print("reprovado")