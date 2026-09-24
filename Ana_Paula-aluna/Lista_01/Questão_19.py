#QUESTÃO 19 - Verificando uma palavra

#Pedido de palavra para o usuário. O que for digitado é atribuído à variável palavra.
palavra = str(input('Digite uma palavra: '))  

if palavra == 'python': 
#Compara se o que foi digitado é exatamento igual a 'python'.
    
    print('Você digitou Python') #Se for igual, mostra essa mensagem.

else:
#Se não for igual...
    
    print('Você digitou outra palavra.') #Se não for igual, mostra essa mensagem.