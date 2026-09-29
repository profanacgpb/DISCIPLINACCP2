name_student = str(input("Digite seu nome: ")).upper() # Entrada de dados string .upper para jogar para minuscúlo
age_student = int(input("Digite sua idade: ")) # Entrada de dados tipo inteiro
grade_student = float(input("Digite sua nota: ")) # Entrada de dados tipo float

print (f"Nome: {name_student}") # Exibição de dadps formatada
print (f"Idade: {age_student}") # Exibição de dados formatada

if age_student >= 18: # Condicional composta
    print ("Situação: Maior de idade")# Exibição de dados
else:
    print ("Situação: Menor de idade") # Exibição de dados
if grade_student >= 7:
    print ("Resultado: Aprovado") # Exibição de dados
else:
    print ("Resultado: Reprovado") # Exibição de dados