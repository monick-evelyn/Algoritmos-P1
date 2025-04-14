populacao_inicial = int(input("Digite o número da população inicial: "))
taxa = float(input("Digite a taxa de crescimento mensal dessa população (em %): "))/100
populacao_total = populacao_inicial

for i in range(60):
    populacao_total = populacao_total + (populacao_total * taxa)
    print(f"Número da população no {i + 1}° mês: {populacao_total:.2f}")
print(f"A população total é: {populacao_total:.2f}")