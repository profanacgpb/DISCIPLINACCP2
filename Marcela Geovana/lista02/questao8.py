dicionario = {
    "Ana": 8.5,
    "Bruno": 7.0,
    "Carlos": 9.0,
    "Daniela": 6.5,
    "Eduardo": 8.0
}

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print(list(dicionario.items())[1])
print(dicionario)

for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")
