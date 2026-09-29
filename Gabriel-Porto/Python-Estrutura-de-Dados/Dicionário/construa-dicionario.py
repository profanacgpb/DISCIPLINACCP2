vermelho = "\033[1;31m"
verde = "\033[1;32m"
reset_cor = "\033[0m"

dados_usuarios = {

}
print ("\n")
print ("-=- Personalização Dicionário -=-")



while (True):
    print ("\n")
    print ("Exemplo: dicionário")
    print ("     nome: Gabriel")
    print ("     idade: 19")
    print ("     curso: Ciência-da-Computação")
    print ("\n")
    print ("Ideias: Idade, Profissão, atribuindo os devidos valores")
    print ("\n")

    keys_dicionario = input("\nDigite o nome do campo (chave): ").strip().lower()
    value_dicionario = input(f"Digite o valor para {keys_dicionario}: ").strip()

    dados_usuarios[keys_dicionario] = value_dicionario

    continuar = input("Deseja adicionar mais um campo (s/n): ").strip().lower()

    if continuar not in ["s", "sim"]:
        break

print (f"\n{verde}Dicionário Cadastrado com sucesso!!!{reset_cor}")

print (dados_usuarios)


print ("\n Campos Personalizados Iterando sobre o dicionário")

for chave, valor in dados_usuarios.items():
    print (f"- {chave}: {valor}")

