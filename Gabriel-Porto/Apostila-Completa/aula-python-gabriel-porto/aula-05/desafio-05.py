print ("\n")
name_complet = str(input("Digite seu nome completo: "))

name_complet_modified = name_complet.split()

for name in name_complet_modified:
    print (name.capitalize().strip(), end = "-")

print ("\n")
