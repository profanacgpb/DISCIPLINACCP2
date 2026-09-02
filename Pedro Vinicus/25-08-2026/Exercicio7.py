media = float(input('Digite a media do aluno: '))
if media >= 7:
    print('Aluno aprovado')
elif media >= 6 and media < 7:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')