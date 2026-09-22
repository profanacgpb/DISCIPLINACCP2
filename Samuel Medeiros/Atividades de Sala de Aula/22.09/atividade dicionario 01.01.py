aluno = {
"nome": "Ana",
"idade": 45,
"cidade": "Campina Grande",
"curso": "Computação"
}
conteudo = input("oque voce quer acessar? ")
if conteudo == "nome":
    print(aluno["nome"])
elif conteudo == "idade":
    print(aluno["idade"])
elif conteudo == "cidade":
    print(aluno["cidade"])
elif conteudo == "curso":
    print(aluno["curso"])
else:
    print("Conteúdo não encontrado. Tente novamente. ")