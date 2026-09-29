pessoas = {
    "nome": "Marcos",
    "idade": 18,
    "cidade": "Campina Grande",
    "curso": "Ciência da Computação",
    "semestre": 2
}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(list(pessoas.items())[1])
print(pessoas)

for chave, valor in pessoas.items():
    print(chave, "tem como valor", valor)