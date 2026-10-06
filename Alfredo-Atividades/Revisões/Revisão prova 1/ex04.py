def conversor():
    reais = float(input("Digite o valor em Reais: "))
    dolar = reais / 5.25
    euros = reais / 6.15
    print("o valor em Dólares é: ", f"{dolar:.2f}", "e o valor em Euros é: ", f"{euros:.2f}")
conversor()