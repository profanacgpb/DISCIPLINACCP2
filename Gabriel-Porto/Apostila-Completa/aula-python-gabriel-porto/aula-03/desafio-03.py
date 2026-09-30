# Faça um programa que calcule o IMC a partir de peso e altura. O foco da aula é entrada, conversão, cálculo e saída.

name = str(input("Digite seu nome: ")).upper()
height = float(input("Digite sua altura em (metros): "))
peso = float(input("Digite seu peso (Kg): "))
imc = (peso) / (height**2)

print (f"Olá {name}, tudo belezinha?")
print (f"Você tem {height:.2f}m e tem {peso:.2f}kg")
print (f"O seu IMC é igual a: {imc:.2f}")