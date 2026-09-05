#Exercicio 4 da aula05 separar nome e sobrenome

nome = "Pedro Vinicius Lima Guimaraes"
partes = nome.split()
primeiro_nome= " ".join(partes[:2])  
sobrenome = " ".join(partes[2:])

print(primeiro_nome)
print(sobrenome)