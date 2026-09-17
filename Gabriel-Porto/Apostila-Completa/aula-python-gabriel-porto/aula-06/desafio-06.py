name_user = str(input("Digite seu nome: ")).upper().strip()

print (f"Olá {name_user}, seja bem-vindo ao laboratório-CLI, para continuar digite LAB: ", end="")
key_shortcut = str(input()).upper().strip()


while key_shortcut == "LAB":
    age_user = int(input("Digite sua idade: "))
    matricula = bool(input())
    if age_user >= 18 and matricula == True:
        print ("Acesso Liberado")
    else:
        print ("Acesso não Autorizado")