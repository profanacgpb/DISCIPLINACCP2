idade = int(float(input("Digite a sua idade: ")))
critico = int(float(input("Qual o nivel critico do paciente? (1 a 10): ")))
if idade < 18 and critico >= 7:
    print("Classificação de atendimento: Urgente")
if idade < 18 and critico < 7:
    print("Classificação de atendimento: Normal Pediatrico")
if idade >= 18 and critico >= 7:
    print("Classificação de atendimento: Urgente")
if idade >= 18 and critico < 7:
    print("Classificação de atendimento: Normal")
if idade >= 50 and critico >= 7:
    print("Classificação de atendimento: Preferencial Urgente")
if idade >= 50 and critico < 7:
    print("Classificação de atendimento: Preferencial")