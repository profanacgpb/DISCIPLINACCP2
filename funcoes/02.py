def converter_reais(valor_reais, moeda):
    if moeda == "dolar":
        cotacao = 5.40
    elif moeda == "euro":
        cotacao = 6.30
    elif moeda == "peso":
        cotacao = 0.004
    else:
        return "Moeda inválida"

    return valor_reais / cotacao


valor = float(input("Digite o valor em reais: "))
moeda = input("Digite a moeda (dolar, euro ou peso): ").lower()

resultado = converter_reais(valor, moeda)

print("Resultado:", resultado)