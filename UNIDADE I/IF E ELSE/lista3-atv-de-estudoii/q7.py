valor = float(input("Digite o valor da compra: "))
desconto = 0
if (valor > 100.0):
    desconto -= valor * 0.1
elif (valor > 200.0):
    desconto -= valor * 0.15
elif (valor > 300.0):
    desconto -= valor * 0.20
else:
    print("Não tem desconto")

print(f"O valor final da compra é R$ {valor:.2f}")