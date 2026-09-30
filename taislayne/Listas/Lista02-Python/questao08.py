celulares = {
    "iPhone": 5000,
    "Samsung": 3000,
    "Motorola": 2000,
    "Xiaomi": 2500,
    "Nokia": 1000
}

print(celulares.keys())

print(celulares.values())

print(celulares.items())

print(list(celulares.items())[1])

print(celulares)

for chave, valor in celulares.items():
    print(f"{chave} tem como valor {valor}")