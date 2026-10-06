def litros():
    distancia=float(input("digite a distância em km: "))
    consumo=float(input("digite o consumo do carro em km/l: "))
    litro=distancia/consumo
    print("O carro irá gastar", f"{litro:.2f}", "litros de combustível.")
litros()    