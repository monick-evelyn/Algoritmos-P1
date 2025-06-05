def conversor_temperatura (temperatura, medida):
    if (medida == "F"):
        temp = (temperatura - 32) / 1.8
        return f"{temp:.2f} °C"
    elif (medida == "C"):
        temp = 1.8*temperatura + 32
        return f"{temp:.2f} °F"
    else:
        return "Medida inválida"
print(conversor_temperatura(32, "F"))
print(conversor_temperatura(100, "C"))