#Faça um sistema de classificação de atendimento com prioridade normal, preferencial e urgente.
atendimento = input("Fale qual exame ira realizar:")

exames = ["Creatinina", "Glicemia de jejum", "Hemoglobina Glicada", "Troponina",
          "Gasometria arterial","Eletrólitos","Beta-HCG", "Culturas bacterianas" ]


exames_normais = ["Creatinina", "Glicemia de jejum", "Hemoglobina Glicada"]
exames_preferencial = ["Beta-HCG", "Culturas bacterianas"]
exames_urgente = [ "Troponina","Gasometria arterial","Eletrólitos"]

if atendimento in exames_normais:
    print(f"Vc veio fazer o exame de {atendimento}. Aguarde que vc sera chamado (Prioridade: Normal).")
elif atendimento in exames_preferencial:
    print(f"Vc veio fazer o exame de {atendimento}. Pode ir realizar o seu exame (Prioridade: Preferencial).")
elif atendimento in exames_urgente:
    print(f"Vc veio fazer o exame de {atendimento}. Uma pessoa ira te atender imediatamente (Prioridade: Urgente).")
else:
    print("Não realizamos esse exame.")