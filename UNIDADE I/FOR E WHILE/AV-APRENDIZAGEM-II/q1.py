num = int(input("Informe um número: "))
maior = num
while (num != 0):
    #print (f"Maior número: {maior}")
    num = int(input("Informe um número: "))
    if (num != 0):
        if (num > maior):
            maior = num
            
print (f"Maior número: {maior}")