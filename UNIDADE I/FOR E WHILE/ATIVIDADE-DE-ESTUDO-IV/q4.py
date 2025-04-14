num = 0
soma = 0
while num >= 0:
    num = int(input("Insira o número positivo (negativo pra parar): "))
    if (num >= 0):
        soma = soma + num
print (f"Soma: {soma}")