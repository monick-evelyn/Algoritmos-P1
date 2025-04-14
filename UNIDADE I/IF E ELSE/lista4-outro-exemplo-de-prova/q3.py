mana = int(input("Informe sua mana disponível: "))

if (mana >= 100):
    print("Bola de fogo")
elif (mana >= 50 and mana < 100):
    print("Cura avançada")
elif (mana >= 20 and mana < 50):
    print("Escudo Mágico")
else:
    print("Descansar e meditar")