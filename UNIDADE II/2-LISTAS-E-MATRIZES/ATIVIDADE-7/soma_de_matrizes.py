matriz1 = [[1,1,1],
           [2,2,2],
           [3,3,3]]
matriz2 = [[1,1,1],
           [2,2,2],
           [3,3,3]]

matriz_resultante = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]

for i in range(3): #linhas
    for j in range (3): #colunas
        matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]

for i in range(3):
    for j in range(3):
        print(matriz_resultante[i][j], end=" ")
    print()