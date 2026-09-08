idade =int(input("digite sua idade: "))
matricula_ativa =input("digite se sua matricula esta ativa? (sim ou não): ")

if idade >= 18 and matricula_ativa == "sim":
    print("você pode entrar no laboratório")
else:
    print("você não pode entrar no laboratório")