#QUESTÃO 18 - Divisível por 5

#Pedido de número inteiro para o usuário. O que for digitado é atribuído à variável numero.
numero = int(input('Digite um número inteiro: '))

if numero%5 == 0:
#Verifica se o resto da divisão do número por 5 é zero.

    print(f'O número {numero} é DIVISÍVEL por 5.') #Se a condição é satisfeita, mostra essa mensagem.

else:
#Se o resto da divisão do número por 5 NÃO FOR zero...

    print (f'O número {numero} NÃO é divisível por 5.')  #Mostra essa mensagem.