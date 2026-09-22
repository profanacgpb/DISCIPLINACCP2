dicionario = {
    "nome": "Yasmim",
    "idade": 18,
    "curso": "Enfermagem",
    "cidade": "Campina Grande",
    "semestre": "1º"
}

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print(list(dicionario.items())[1])
print(dicionario)

for chave, valor in dicionario.items():
    print(chave, "tem como valor", valor)
