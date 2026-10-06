def usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    curso = input("Digite seu curso: ")
    semestre = int(input("Digite seu semestre: "))
    
    print(f"Olá, {nome}! Você tem {idade} anos, estuda {curso} e está no {semestre}º semestre.")
usuario()