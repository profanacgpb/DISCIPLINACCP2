vermelho = "\033[1;31m"
verde = "\033[1;32m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
reset_cor = "\033[m"

def exibicao_menu ():
    print ("-=-" * 10)
    print ("     (1) SAUDAÇÃO")
    print ("     (2) CALCULAR MEDIA")
    print ("     (3) VERIFICAR SITUAÇÃO")
    print ("-=-" * 10)

print ("\n")
print ("SEJA BEM-VINDO AO SISTEMA DE NOTAS 2.0 PATRÃO")

name_student = str(input("Digite seu nome: ")).upper()
nota_1, nota_2, nota_3 = map(float, input("Digite suas notas (respectivamente com espaços) Ex: 7.0 8.0 5.0: ").split())

print ("\n")
print (f"{ciano}O que você quer fazer em seguida? segue o menu abaixo:{reset_cor}")

exibicao_menu ()

escolha_usuario = int(input("Escolha umas das opções acima: "))

# Funções definidas depois do programa porque se eu definir antes como vou passar os parâmetros
def saudacao (nome):
    print (f"{ciano}Olá {nome}, falaaa cuida chama no python{reset_cor}")

def calcular_media (entrada_nota_1, entrada_nota_2, entrada_nota_3):
    media_entrada = (entrada_nota_1 + entrada_nota_2 + entrada_nota_3) / 3
    print (f"{amarelo}A sua média é igual a: {media_entrada:.2f}{reset_cor}")
    return media_entrada # Return guarda um valor para a função

def verificar_situacao ():
    if calcular_media (nota_1, nota_2, nota_3) >= 7:
        print (f"{verde}Parabéns você foi APROVADO!!!{reset_cor}")
    else:
        print (f"{vermelho}É fogo mano relaxa que vai dar certo porque errado já deu você foi REPROVADO!!!{reset_cor}")

tentativas_loop = 0

while (escolha_usuario != 1 or escolha_usuario != 2 or escolha_usuario != 3):
    if escolha_usuario == 1:
        saudacao (name_student)
        break
    elif escolha_usuario == 2:
        calcular_media (nota_1, nota_2, nota_3)
        break
    elif escolha_usuario == 3:
        verificar_situacao ()
        break
    else:
        print (f"{vermelho}Você digitou {escolha_usuario}!!!{reset_cor}")
        for loop in range (1, 4, +1):
            tentativas_loop += 1
            escolha_usuario = int(input(f"Escolha uma das opções acima (novamente) (você possui 3 tentativas) (você está com {loop} tentativas): "))
            if tentativas_loop >= 3:
                print (f"{vermelho}Você excedeu o números de tentativas{reset_cor}")
                print (f"{verde}Programa Finalizado{reset_cor}")
                break
        break