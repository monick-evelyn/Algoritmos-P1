
def soma_matriz (matriz, indice):
    return sum(matriz[indice])
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
indice = 2
print(soma_matriz(matriz, indice)) #7 + 8 + 9 = 24

#somar por coluna:
linhas = 3
soma = 0
for i in range(linhas):
    soma += matriz[i][0]
print(soma) #1 + 4 + 7 = 12
