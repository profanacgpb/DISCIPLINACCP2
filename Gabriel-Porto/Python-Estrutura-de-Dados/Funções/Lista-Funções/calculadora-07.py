valor_entrada_1, valor_entrada_2 = map(int, input("Digite dois números inteiros aleatórios (respectivamente): ").split())

def somar (entrada_1, entrada_2):
    soma = entrada_1 + entrada_2
    return soma

def subtrair (entrada_1, entrada_2):
    subtrai = entrada_1 - entrada_2
    return subtrai

def multiplicar (entrada_1, entrada_2):
    multiplica = entrada_1 * entrada_2
    return multiplica

def dividir (entrada_1, entrada_2):
    dividi = entrada_1 / entrada_2
    return dividi

print ("Já com os dois números digitados respectivamente qual operação você quer fazer menu logo abaixo:")

print ("-=-" * 10)
print ("     (1) SOMAR")
print ("     (2) SUBTRAIR")
print ("     (3) MULTIPLICAR")
print ("     (4) DIVIDIR")
print ("-=-" * 10)

escolha_menu = int(input("Escolha uma das opções acima: "))

while (escolha_menu != 1 or escolha_menu != 2 or escolha_menu != 3 or escolha_menu != 4):
    if escolha_menu == 1:
        exibicao = somar (valor_entrada_1, valor_entrada_2)
        print (f"A soma entre {valor_entrada_1} e {valor_entrada_2} é {exibicao} (respectivamente)")
        break
    elif escolha_menu == 2:
        exibicao = subtrair (valor_entrada_1, valor_entrada_2)
        print (f"A subtração entre {valor_entrada_1} e {valor_entrada_2} é {exibicao} (respectivamente)")
        break
    elif escolha_menu == 3:
        exibicao = multiplicar (valor_entrada_1, valor_entrada_2)
        print (f"A multiplicação entre {valor_entrada_1} e {valor_entrada_2} é {exibicao} (respectivamente)")
        break
    elif escolha_menu == 4:
        exibicao = dividir (valor_entrada_1, valor_entrada_2)
        print (f"A divisão entre {valor_entrada_1} e {valor_entrada_2} é {exibicao} (respectivamente)")
        break
    else:
        print (f"Você digitou {escolha_menu}")
        escolha_menu = int(input("Escolha uma das opções acima (novamente): "))
