dicionario = {
    "nome": "Gustavo",
    "idade": 20,
    "curso": "Enfermagem",
    "cidade": "Campina Grande",
    "semestre": 1
}


print(dicionario.keys())


print(dicionario.values())


print(dicionario.items())


print(list(dicionario.items())[1])


print(dicionario)


for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")