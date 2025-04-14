valor_inicial = float(input("Informe o valor inicial do depósito: "))
taxa_anual = float(input("Informe a taxa de juros anual (em %): "))
anos = int(input("Informe o número de anos: "))

meses = anos * 12
valor_total = 0
taxa_mensal = taxa_anual / 12

for i in range (0, meses, 1):
    valor_inicial = valor_inicial + (valor_inicial * (taxa_mensal/100))
    print(f"Valor no {i + 1}° mês: {valor_inicial:.2f}")
print(f"O valor total após {meses} meses é de R$ {valor_inicial:.2f}")