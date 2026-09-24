from time import sleep # Importação apenas de um comando específico da biblioteca time
value_user1 = int(input("Digite um número para exibir a tabuada (1x10): ")) # Entrada de dados

# for: usando for
for loop in range (1, 11, +1):
    resultado = value_user1*loop
    sleep (1)
    print (f"{value_user1} x {loop} = {resultado}")

# while: usando while
value_user2 = int(input("Digite um número para exibir a tabuada (1x10): ")) # Entrada de dados
loop = 0 # Definição antes do loop

while (loop <= 9): # Enquanto o loop for menor ou igual a 9 faça loop = loop + 1
    loop += 1
    resultado = value_user2*loop # Variável para armazenar
    sleep (1)
    print (f"{value_user2} x {loop} = {resultado}")