altura =input("Qual a sua altura em METROS: ")
peso = input("Qual o seu peso em kg: ")
imc = float(peso)/float(altura)**2
print(imc * 10**4) #o resultado do imc é multiplicado por 10^4 para ficar mais legível, pois o resultado do imc é um número muito pequeno.