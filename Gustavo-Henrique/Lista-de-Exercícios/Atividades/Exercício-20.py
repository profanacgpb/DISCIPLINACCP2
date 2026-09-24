# Verificação de dados de um aluno

Nome = input('Digite seu nome: ')
Idade = int(input('Digite sua idade: '))
Nota = int(input('Digite sua nota: '))
if Nota >= 7 and Idade >= 18:
    print(f' Nome: {Nome}\n idade: {Idade}\n Situação: Maior de Idade\n Resultado: Aprovado ')
if Nota >= 7 and Idade < 18:
    print(f' Nome: {Nome}\n idade: {Idade}\n Situação: Menor de Idade\n Resultado: Aprovado ')
if Nota < 7 and Idade < 18:
    print(f' Nome: {Nome}\n idade: {Idade}\n Situação: Menor de Idade\n Resultado: Reprovado ')
if Nota < 7 and Idade >= 18:
    print(f' Nome: {Nome}\n idade: {Idade}\n Situação: Maior de Idade\n Resultado: Reprovado ')

    # Explicação: 
    # Primeiro peço o nome do usuário, sua idade e a nota
    # Em seguida é feita uma verificação de parâmetros Utilizando if´s
    # Após essa verificação o programa mostra o resultado de acordo de acordo com as informações dadas