nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
n = int(input("Digite a sua nota: "))

print (f"Nome: {nome}")
print (f"Idade: {idade}")
if idade >= 18:
    print ("Situação: maior de idade")
elif idade <18:
    print ("Situação: menor de idade")
if n >= 7:
    print ("Resultado: Aprovado")
elif n < 7:
    print ("Resultado: Reprovado")