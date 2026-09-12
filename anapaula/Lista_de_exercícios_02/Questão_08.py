#QUESTÃO 8: Crie um dicionário com 5 entradas e suas respectivas chaves e valores. Faça: 

dicionario_animais = {
    "Animal": "Leão",
    "Habitat": "Savanas e regiões de pastagem da África",
    "Alimentacao": "Carne",
    "Expectativa de vida": "De 10 a 15 anos",
    "Velocidade aproximada (em km/h)": 80
}

#Letra a: Imprima todas as chaves do dicionário
print("CHAVES:", dicionario_animais.keys())

#Letra b: Imprima todos os valores do dicionário
print("VALORES:", dicionario_animais.values())

#Letra c: Imprima todos os itens do dicionário 
print("ITENS:", dicionario_animais.items())

#Letra d: Imprima o 2º item do dicionário 
print("\nSegundo item: ")
i = 0
for chave, valor in dicionario_animais.items():
    i = i + 1
    if i == 2:
        print (f"Chave {chave} tem como valor {valor}.")

#Pesquisando, encontrei esta outra forma de fazer a letra d (utilizando list):
print("SEGUNDO ITEM:", list(dicionario_animais.items())[1])
print("\n")

#letra e: Imprima o dicionário completo 
print("DICIONÁRIO COMPLETO: ", dicionario_animais)
print("\n")

#Letra f: Percorra o dicionário, imprimindo para cada entrada o modelo “(chave) tem como valor (valor)”
i = 0
for chave, valor in dicionario_animais.items():
    print (f"Chave {chave} tem como valor {valor}.")
    i = i+1

#Letra f: no modelo chave valor
print("\nITENS NO FORMATO: CHAVE VALOR")
for chave, valor in dicionario_animais.items():
    print(chave, valor)

#Letra f utilizando list para mostrar cada item da forma (chave, valor)
print("\nITENS NO FORMATO: (Chave, Valor):")

for i in range(len(dicionario_animais)):
    print(f"Item {i+1}:", list(dicionario_animais.items())[i])


