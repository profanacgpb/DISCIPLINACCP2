# codigo começa com um comando de entrada  pedindo uma palavra qualquer ao usuário.

palavra = input("Digite uma palavra: ")

# se a palavra digitada pelo usuario atender a condição do if, ele vai executar o primeiro print.

if palavra == "python":
    print("Você digitou Python!")

# se não atender a condição ele vai entrar no else e executar o segundo print

else:
    print("Você digitou outra palavra.")