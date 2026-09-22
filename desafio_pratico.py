Aluno={
    "nome":".",
    "idade":".",
    "curso": "."
}
Aluno["nome"] = input('Digite nome:')
Aluno["idade"] = input('Digite idade:')
Aluno["curso"] = input('Digite curso:')

Aluno2={
    "nome":".",
    "idade":".",
    "curso": "."
}
Aluno2["nome"] = input('Digite nome:')
Aluno2["idade"] = input('Digite idade:')
Aluno2["curso"] = input('Digite curso:')

lista = [Aluno["nome"], Aluno["idade"], Aluno["curso"]]
print(lista)
lista2 = [Aluno2["nome"], Aluno2["idade"], Aluno2["curso"]]
print(lista2)


arquivo = open('arquivo_desafio.txt', 'w')
arquivo.write(str(lista))
arquivo.write(str(lista2))

