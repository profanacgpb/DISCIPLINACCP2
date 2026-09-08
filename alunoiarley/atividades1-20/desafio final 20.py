name_student = str(input("Digite seu nome: ")).upper() 
age_student = int(input("Digite sua idade: ")) 
grade_student = float(input("Digite sua nota: ")) 

print (f"Nome: {name_student}") 
print (f"Idade: {age_student}") 

if age_student >= 18: 
    print ("Situação: Maior de idade")
else:
    print ("Situação: Menor de idade") 
if grade_student >= 7:
    print ("Resultado: Aprovado")
else:
    print ("Resultado: Reprovado") 