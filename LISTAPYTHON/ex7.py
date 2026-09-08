nome = input("Olá, digite seu nome: ")

notas = []

for i in range(3):
    nota = float(input(f"Olá, {nome}. Digite sua {i+1}ª nota: "))
    notas.append(nota)


media = sum(notas) / len(notas)

if media >= 7:
    print(f"Parabéns {nome}, você foi aprovado por média!")
elif media < 7 and media > 5:
    print(f"{nome}, como sua nédia foi: {media}, você vai ter que fazer PROVA FINAL")
else:
    print(f"Que pena {nome}, você foi REPROVADO")