#Questão 4 - Números
with open("numeros1.txt", "w") as numeros:
    for numero in range(1,21):
        numeros.write(f"{numero}\n")