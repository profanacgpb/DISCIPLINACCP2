#Faça um programa que calcule o IMC a partir de peso e altura. O foco da aula é entrada, conversão, cálculo e saída.
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
print(f"Peso: {peso}\nAltura: {altura}\nIMC: {imc:.2f}\n")