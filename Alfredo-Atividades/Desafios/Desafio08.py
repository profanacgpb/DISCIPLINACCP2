for numero in range(1, 11):
    print(f"--- Tabuada do {numero} ---")   #--- so como decoração no terminal, ficaria ---tabuada do 1--- como exemplo
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()