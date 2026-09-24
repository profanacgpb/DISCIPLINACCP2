#Faça um programa que calcule o IMC a partir de peso e altura. O foco da aula é entrada, conversão, cálculo e saída.

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em M: "))

calculo = peso / (altura ** 2)

print(f"{nome}, o seu IMC é: {calculo:.2f}")
