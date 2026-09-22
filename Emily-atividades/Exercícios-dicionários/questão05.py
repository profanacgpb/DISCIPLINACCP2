aluno = {
    "nome": "Emily",
    "idade": 18, 
    "cidade": "Campina Grande",
    "curso": "Ciências da Computação"
}

aluno["idade"] = 20
aluno["curso"] = "Psicologia"

aluno["e-mail"] = "fulanodetal@gmail.com"
aluno["telefone"] = "83996797208"

aluno.pop("telefone")

if "e-mail" in aluno:
    print ("A chave e-mail existe!")