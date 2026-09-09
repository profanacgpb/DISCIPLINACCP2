# Faça um sistema de classificação de atendimento com prioridade normal, preferencial e urgente.

nome = input("Digite seu nome: ")

print("--------OPÇÕES--------")
print("(1) para Normal")
print("(2) para Prioridade")
print("(3) para Urgente")

prioridade = int(input("Digite um dos números acima em referência a sua prioridade: "))

if prioridade == 1:
    print(f"{nome}, você escolheu a opção (1), então seu atendimento vai ser NORMAL")

elif prioridade == 2:
    print(f"{nome}, você escolheu a opção (2), então seu atendimento vai ser PRIORIDADE")

else:
    print(f"{nome}, você escolheu a opção (3), então seu atendimento vai ser URGENTE")
    

