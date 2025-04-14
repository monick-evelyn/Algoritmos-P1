mes = int(input("Digite o número de um mês do ano (número): "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Mês com 31 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Mês com 30 dias")
elif mes == 2:
    print("Mês com 28/29 dias")
else:
    print("Mês inválido!")