nota = -1
contador = 0
soma = 0
while (nota < 0 or nota > 10 or contador < 2):
    nota = float(input(f"Digite a {contador + 1}° nota: "))
    if (nota < 0 or nota > 10):
        print("Nota com valor inválido!")
    else:
        contador += 1
        soma += nota
print(f"Notas válidas! A média é {soma/contador:.1f}")