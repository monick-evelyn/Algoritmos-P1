velocidade_gato = float(input("Digite a velocidade do gato (Km/h): "))

if velocidade_gato < 5:
    classificacao = "Gato preguiçoso"
elif velocidade_gato >= 5 and velocidade_gato <= 15:
    classificacao = "Gato normal"
else:
    classificacao = "Gato turbo! Cuidado!"

print(f"{classificacao}")