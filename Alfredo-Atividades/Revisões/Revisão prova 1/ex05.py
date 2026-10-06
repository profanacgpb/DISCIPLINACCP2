def frase():
    frases = input("digite uma frase: ").strip()
    print(frases.upper())
    print(len(frases))
    if "python" in frases.lower():
        print("A palavra 'python' está presente na frase.")
    else:
        print("A palavra 'python' não está presente na frase.")
frase()