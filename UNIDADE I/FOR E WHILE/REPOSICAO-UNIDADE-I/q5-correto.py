quadrado = 1 # 1 quadrado
print(f"1º possui {quadrado} grão") #1
soma = 1 
for i in range(2, 65):
    quadrado = quadrado * 2
    print(f"{i}º possui {quadrado} grãos")
    soma += quadrado
print(f"O total de grãos no xadrez é {soma}")