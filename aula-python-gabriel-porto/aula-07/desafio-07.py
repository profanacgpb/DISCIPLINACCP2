# Faça um sistema de classificação de atendimento com prioridade normal, preferencial e urgente.


print ("========================")
print ("SISTEMA DE CLASSIFICAÇÃO")
print ("========================")

print ("TIPOS DE EXAMES:")

print ("Creatinina (1)")
print ("Glicemia de jejum (2)")
print ("Hemoglobina Glicada (3)")
print ("Troponina (4)")
print ("Gasometria arterial (5)")
print ("Eletrólitos (6)")
print ("Beta-HCG (7)")
print ("Culturas bacterianas (8)")

tipo_exame = int(input("Digite qual o tipo do teu exame seguindo o menu a seguir: "))

if tipo_exame == 1:
    print ("Prioridade Normal")
elif tipo_exame == 2:
    print ("Prioridade Normal")
elif tipo_exame == 3:
    print ("Prioridade Normal")
elif tipo_exame == 4:
    print ("Prioridade Urgente")
elif tipo_exame == 5:
    print ("Prioridade Urgente")
elif tipo_exame == 6:
    print ("Prioridade Urgente")
elif tipo_exame == 7:
    print ("Prioridade Preferencial")
elif tipo_exame == 8:
    print ("Prioridade Preferencial")
else:
    print ("Não existe essa escolha nesse menu renicie o código e tente novamente")