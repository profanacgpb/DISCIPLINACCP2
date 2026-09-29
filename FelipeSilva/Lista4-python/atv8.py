dicionario = {
    "nome": "Felipe",
    "idade": 23,
    "curso": "Ciência da Computação",
    "periodo": 2,
    "cidade": "Ingá"
}

print("8a:", dicionario.keys())

print("8b:", dicionario.values())

print("8c:", dicionario.items())

print("8d:", list(dicionario.items())[1])

print("8e:", dicionario)

for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")