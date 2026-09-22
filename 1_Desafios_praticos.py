frutas=['maça', 'banana', 'uva', 'melão', 'morango']
print(frutas)

adicionar=input('Adicione uma palavra:')
frutas.append(adicionar)
print(frutas)

remover=input('Remova uma palavra:')
frutas.remove(remover)
print(frutas)

alterar=input('Altere o 3° nome:')
frutas[2]=alterar
print(frutas)

frutas1=(frutas[0:3])
frutas2=(frutas[3:5])
print(f'{frutas1} | {frutas2}')

frutas1.reverse()
frutas2.reverse()
print(f'{frutas1} | {frutas2}')

