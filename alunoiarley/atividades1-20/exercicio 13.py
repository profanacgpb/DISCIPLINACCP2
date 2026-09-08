from time import sleep 
value_user1 = int(input("Digite um número para exibir a tabuada (1x10): ")) 

for loop in range (1, 11, +1):
    resultado = value_user1*loop
    sleep (1)
    print (f"{value_user1} x {loop} = {resultado}")

value_user2 = int(input("Digite um número para exibir a tabuada (1x10): ")) 
loop = 0 

while (loop <= 9): 
    loop += 1
    resultado = value_user2*loop 
    sleep (1)
    print (f"{value_user2} x {loop} = {resultado}")