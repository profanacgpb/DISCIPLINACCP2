# Análise de notas:

notas = [7.5, 8.0, 6.5, 9.0, 5.5]

print ("\n")
notas.sort()
print ("Os 3 maiores: ")
print (notas [4])
print (notas [3])
print (notas [2])
print ("\n")

print ("O menor valor: ")
notas.reverse()
print (notas [4])
print ("\n")

soma = (notas [0] + notas [1] + notas [2] + notas [3] + notas [4])
print("A soma é igual a:", soma)

media = soma / 5
print("A média é igual a:", media)

quantidade_lista = len(notas)
print ("A quantidade item na lista é:", quantidade_lista)
print ("\n")