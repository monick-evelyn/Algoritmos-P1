peso = float(input("Informe o peso do animal (em kg): "))

if peso < 10:
    print("Deixe-o passar, é apenas um passarinho!")
elif peso >= 10 and peso <= 50:
    print("Atenção, mas não é tão pesado.")
else:
    print("Alerta! Esse animal pode quebrar o gelo!")