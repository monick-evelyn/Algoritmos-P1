qualidade = int(input("Informe a qualidade da banana em um número de 1 a 10: "))

if (qualidade >= 8 and qualidade <= 10):
    print("Banana premium")
elif (qualidade >= 5 and qualidade <= 7):
    print("Banana regular")
elif (qualidade < 5 and qualidade > 0):
    print("Banana Duvidosa")
else:
    print("Qualidade inválida! Digite um número de 1 a 10.")