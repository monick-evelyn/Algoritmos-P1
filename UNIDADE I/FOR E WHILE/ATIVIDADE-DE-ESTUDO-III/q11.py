preco_inicial = int(input("Informe o preço do carro: "))
taxa_depreciacao = float(input("Informe a taxa de depreciação mensal (em %): "))/100
meses = int(input("Informe o número de meses: "))
preco_total = preco_inicial
for i in range(meses):
    preco_total = preco_total - (preco_total * taxa_depreciacao)
    print(f"Valor no {meses + 1}° mês: R$ {preco_total:.2f}")

print(f"Valor total: R$ {preco_total:.2f}")