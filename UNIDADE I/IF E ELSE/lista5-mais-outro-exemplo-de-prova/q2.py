horario = int(input("Digite o horário (em horas, formato 24h): "))

if (horario >= 8 and horario <= 12):
    print("Promoção ativa! 50% de desconto.")
else:
    print("Volte durante a promoção.")