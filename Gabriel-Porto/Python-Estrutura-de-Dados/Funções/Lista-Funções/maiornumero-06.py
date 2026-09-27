valor_1, valor_2 = map(int, input("Digite dois valores inteiros aleatório (1) (2) (respectivamente): ").split())

def maior_numero (entrada_1, entrada_2):
    if entrada_1 > entrada_2:
        print (f"O maior é {entrada_1}")
    elif entrada_2 > entrada_1:
        print (f"O maior é {entrada_2}")
    else:
        print (f"O valor {entrada_1} é igual a {entrada_2}")


maior_numero (valor_1, valor_2)