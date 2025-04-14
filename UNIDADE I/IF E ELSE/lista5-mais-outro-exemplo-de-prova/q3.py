temperatura = float(input("Informe a temperatura em ºC: "))

if (temperatura >= 30):
    print("Use roupas leves.")
elif (temperatura >= 20 and temperatura <= 29):
    print("Vista algo confortável.")
else:
    print("Use casacos e roupas quentes")