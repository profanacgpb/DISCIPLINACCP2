notas=[7.5,8.0,6.5,9.0,5.5]

print("maior nota:",max(notas))
print("menor nota:",min(notas))
print("quantidade de notas:",len(notas))
print("soma das notas:",sum(notas))
print("média das notas:",sum(notas)/len(notas))
print("notas em ordem:" ,sorted(notas))
print("As três maiores notas são:",sorted(notas, reverse=True)[:3])
