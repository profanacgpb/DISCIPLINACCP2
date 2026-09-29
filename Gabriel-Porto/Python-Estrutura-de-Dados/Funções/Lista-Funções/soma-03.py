valor_1, valor_2 = map (float, input("Digite dois números para ser somados (na mesma linha): ").split())

def soma (valor_entrada1, valor_entrada2):
    resultado = valor_entrada1 + valor_entrada2
    return resultado

resultado  = soma (valor_1, valor_2)

print (f"A soma entre {valor_1:.2f} e {valor_2:.2f} é igual a {resultado:.2f}")