#Questão 4 — Números
#Crie numeros.txt, escreva os números de 1 a 20, um por linha, e depois leia e mostre os números.

arquivo = open("numeros.txt", "w")
for numero in range(1, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()