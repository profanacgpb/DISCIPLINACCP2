dicionario = {'nome': 'Samuel', 'idade': 20, 'curso': 'Python', 'nota': 9.5, 'aprovado': True}

print("\n8a. Chaves:", dicionario.keys())

print("8b. Valores:", dicionario.values())

print("8c. Itens:", dicionario.items())

print("8d. 2º item:", list(dicionario.items())[1])

print("8e. Dicionário completo:", dicionario)

print("8f. Iteração formatada:")
for chave, valor in dicionario.items():
    print(f"({chave}) tem como valor ({valor})")