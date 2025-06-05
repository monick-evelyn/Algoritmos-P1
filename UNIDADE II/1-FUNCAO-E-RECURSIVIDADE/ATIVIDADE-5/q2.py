def preco_passagem (distancia):
    if (distancia < 0):
        return("Distância inválida")
    elif (distancia <= 200):
        return 0.5 * distancia
    else:
        return 0.65 * distancia
print(preco_passagem(200))
print(preco_passagem(201))
print(preco_passagem(-1))
print(preco_passagem(1))