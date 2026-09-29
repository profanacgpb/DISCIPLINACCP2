# Crie uma regra de acesso a um laboratório: idade mínima de 18 anos e matrícula ativa.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
matricula = True

if idade >= 18 and matricula == True:
    print(f"Muito bem {nome}, acesso ao laboratório LIBERADO")
else:
    print(f"Acesso ao laboratório NEGADO")
