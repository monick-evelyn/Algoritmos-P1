def contarpalavras (s):
    vogais = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
    return vogais
print(contarpalavras("Booom dia"))