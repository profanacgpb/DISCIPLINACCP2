while True:
    print("=======CALCULADORA========")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        
        a = int(input("Digite o primeiro numero:"))
        b= int(input("Digite o segundo numero:"))
        
        def somar(a,b):
            return (a + b)
        
        print(f"A soma dos dois numeros é: {somar(a,b)}")
        
    elif opcao == "2":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        def subtrair(a, b):
            return a - b

        print(f"A subtração é: {subtrair(a, b)}")

    elif opcao == "3":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        def multiplicar(a, b):
            return a * b

        print(f"A multiplicação é: {multiplicar(a, b)}")
        
    elif opcao == "4":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        
        if b == 0:
            print("Não é possivel dividir por zero.")
        else:
            def dividir(a,b):
                return a/b
            
            print(f"A divisão é:{dividir(a,b)}")
           
    elif opcao == "5":
        print("Calculadora encerrada.")
        break