quadrados = 1
soma = 1
for i in range(2, 64 + 1):
    quadrados = quadrados * 2
    soma += quadrados
print(soma)