quant_kwh = float(input("Informe a quantidade de kWh consumida: "))
instalacao = str(input("Informe o tipo de instalação: ")).upper()

preco = 0.0
if instalacao == "RESIDENCIAL":
    if quant_kwh <= 500:
        preco = quant_kwh * 0.40
    elif quant_kwh > 500:
        preco = quant_kwh * 0.65
elif instalacao == "COMERCIAL":
    if quant_kwh <= 1000:
        preco = quant_kwh * 0.55
    elif quant_kwh > 1000:
        preco = quant_kwh * 0.60
elif instalacao == "INDUSTRIAL":
    if quant_kwh <= 5000:
        preco = quant_kwh * 0.55
    elif quant_kwh > 5000:
        preco = quant_kwh * 0.60
else:
    print("Instalação informada inválida!")

print(f"O preço a pagar é de R$ {preco:.2f}")