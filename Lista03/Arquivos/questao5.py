#Questão 5 - Append
with open("numeros1.txt", "a") as numeros:
    for numero in range(22,31):
        numeros.write(f"{numero}\n")