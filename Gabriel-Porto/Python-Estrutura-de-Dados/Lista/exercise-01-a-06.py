# 1. Crie uma lista com números de 0 a 9 (em qualquer ordem).
  
numbers = [0, 1, 2, 3, 5, 7, 8, 9]

print ("\n")
print (f"Lista Inicial {numbers}")
print ("\n")
numbers.append(6)
print (f"Adicionando o 6 {numbers}")
print ("\n")
numbers.insert (2, 7)
print (f"Inserir o número 7 {numbers}")
print ("\n")
numbers.append(4)
print (f"Adicionando o número 4 {numbers}")
print ("\n")
quantidade_ocorrencias = numbers.count(4)
print (f"A quantidade de ocorrências é {quantidade_ocorrencias}")
print ("\n")

# 2. Ainda com a lista criada na questão anterior, faça:

print ("\n")
print (numbers [:3])
print (numbers [2:6])
print (numbers [::3])
print (numbers [-3:])
print (numbers [::-4])
print ("\n")

# 3. Com a lista das questões anteriores, retorne o sexto elemento da lista:

print (f"Retornando o sexto elemento: {numbers [5]}")

# 4. Altere o valor do sétimo elemento da lista para o valor 12

numbers.insert (7, 12)
print (f"Adicionando o sétimo elemento para o valor 12 {numbers}")

# 5. Inverta a ordem dos elementos lista

numbers.reverse()
print (f"Lista invertida: {numbers}")

# 6. Ordene a lista

numbers.sort()
print (f"Lista Ordenada: {numbers}")