notas= [7.5, 8.0, 6.5, 9.0, 5.5]
maiornota= max(notas)
print("Sua maior nota é:", maiornota)

menornota= min(notas)
print("Sua menor nota é:", menornota)

quantidade= len(notas)
print("Você ja recebeu:", quantidade, "notas!")

soma= sum(notas)
print("A soma de todas as notas é:", sum(notas))

media= len(notas)
print("Sua media é de:", len(notas))

notas_ordenadas=[]
for i in range(len(notas)):
    menor = min(notas)
    notas_ordenadas.append(menor)
    notas.remove(menor)
print(notas_ordenadas)

notas = [7.5, 8.0, 6.5, 9.0, 5.5] 
maiores_valores=[]
for p in range(3):
    maior=max(notas)
    maiores_valores.append(maior)
    notas.remove(maior)
print(maiores_valores)
