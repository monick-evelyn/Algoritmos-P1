temperatura = float(input("Digite a temperatura da geladeira em °C: "))

if (temperatura < 0):
    print("Comida congelado. Que tal um sorvete?")
elif(temperatura >= 0 and temperatura <= 5):
    print("Tudo em ordem!")
else:
    print("Comida estragando! Ligue o técnico!")