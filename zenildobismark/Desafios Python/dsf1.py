#Crie um programa que imprima seu nome, curso, período e uma frase sobre o que você espera aprender em Python.

nome = input("Digite seu nome: ")
curso = input("Digite seu curso: ")
período = int(input("Digite seu período: "))
frase = input("O que você espera aprender com Python? :")

print(f"Oi, me chamo {nome}. Estou cursando {curso} ({período}° período) na UNINASSAU, e {frase} ")