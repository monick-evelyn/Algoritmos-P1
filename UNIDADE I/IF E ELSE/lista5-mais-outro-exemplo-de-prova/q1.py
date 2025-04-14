humor = str(input("Informe sue humor (feliz, neutro ou bravo): ")).upper()

if (humor == "FELIZ"):
    print("Deixe 20% do total da conta.")
elif (humor == "NEUTRO"):
    print("Deixe 10% do total da conta.")
elif (humor == "BRAVO"):
    print("Gorjeta opcional")
else:
    print("Humor inválido! Escolha entre feliz, neutro ou bravo.")