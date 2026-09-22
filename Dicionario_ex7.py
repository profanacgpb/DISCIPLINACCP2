aluno = {
    "nome": "João",
    "nota1": int(8),
    "nota2": int (6)
}
media= (aluno["nota1"]+ aluno["nota2"]) /2
print(f"Media:{media}" )
if media >= 7:
    print("Você foi aprovado!")
else:
    print ("Você foi reprovado")
