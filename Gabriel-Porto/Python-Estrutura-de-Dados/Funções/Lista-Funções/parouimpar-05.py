valor_usuario = int(input("Digite um valor inteiro: "))

def par_ou_impar (random_value):
    if random_value % 2 == 0:
        print (f"O valor {random_value} é PAR")
    else:
        print (f"O valor {random_value} é IMPAR")

par_ou_impar (valor_usuario)