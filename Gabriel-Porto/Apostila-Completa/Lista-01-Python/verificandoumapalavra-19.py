word_user = str(input("Digite uma palavra qualquer: ")).lower()
# tipo primitivo string iusando um método para deixar tudo minusculo evitar que o usuário digite em maiúsculo
amarelo = "\033[33m" # cores da tabela ansi
vermelho = "\033[31m" # cores da tabela ansi
fim_cor = "\033[0m" # cores da tabela ansi

if word_user == "python": # Verificação da palavra python para garantir que tudo vai estar em minuscúlo
    print (f"{amarelo}Você digitou python{fim_cor}") # Exibição de dados
else: # Senão
    print (f"{vermelho}Você digitou outra palavra{fim_cor}") # Exibição de dados