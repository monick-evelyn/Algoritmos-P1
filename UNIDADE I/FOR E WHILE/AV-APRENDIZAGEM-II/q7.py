quant = int(input("Informe quantos números serão somados: "))
termo1 = int(input("Informe o 1° termo da sequência: "))
soma = 0
contador = 0
while (contador < quant):
    #for i in range (termo1, quant + 1, 1):
    print(f"{soma} + {termo1} = {soma + termo1}")
    soma += termo1
    contador += 1
    termo1 += 2

print(f"Soma dos números: {soma}")