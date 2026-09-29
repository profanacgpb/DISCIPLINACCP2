# Crie um programa que receba um nome completo e produza uma versão normalizada: sem espaços extras e com 
# iniciais em maiúsculas.

nome = input("Digite seu nome: ")

nomemod = " ".join(nome.split()).title()

print(nomemod)