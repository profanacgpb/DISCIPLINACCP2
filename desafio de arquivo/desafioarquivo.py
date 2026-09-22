Aluno={
    "nome":".",
    "idade": ".",
    "curso": "."
}
Aluno["nome"] = input('digite seu nome: ')
Aluno["idade"] = input('digite sua idade: ')
Aluno["curso"] = input('digite seu curso: ')

Aluno2={
    "nome":".",
    "idade": ".",
    "curso": "."
}
Aluno2["nome"] = input('digite seu nome: ')
Aluno2["idade"] = input('digite sua idade: ')
Aluno2["curso"] = input('digite seu curso: ')

lista = [Aluno["nome"],Aluno["idade"],Aluno["curso"]]
print(lista)
lista2 = [Aluno2["nome"],Aluno2["idade"],Aluno2["curso"]]
print(lista2)

arquivo = open('desafioarquivo.txt', 'w')
arquivo.write(str(lista))
arquivo.write(str(lista2))