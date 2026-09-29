peso = input ("Digite o seu peso em kg: ")
altura = input ("Digite a sua altura em metros: ")
imc = float(peso) / (float(altura) ** 2)
print("O seu IMC é: ", f"{imc:.2f}")