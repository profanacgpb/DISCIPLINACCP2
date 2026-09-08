#Criar uma regra de acesso a um laboratorio:idade minimma de 18 anos e matrícula ativa
idade = int(input("Digite sua idade:")) 

matricula = input("Digite o status da sua matricula (0/1): ")

#Usei a estrutura de condição para mostra diferentes forma que pode acontecer na questão de acesso
if idade >= 18 and matricula == "1": #caso tenha todos os requisitos pode acessar
    print("Pode acessar")
elif idade >= 18 and matricula == "0": #Caso tenha a idade mais não tem a matricula ativa
    print("Sua matricula não esta ativa. Verifique com o seu supervisor")
else: #Caso não tenha idade menor ou matricula de acesso  não pode acessar
    print("Não tem acesso")


