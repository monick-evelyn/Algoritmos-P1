horas = 0
soma = 0
contador = 0
media = 0
while horas >= 0:
    horas = int(input("Digite o número de horas trabalhas (negativo pra parar): "))
    if (horas >= 0):
        soma += horas
        contador += 1
if (contador > 0):
    media = soma/contador
print(f"O total de horas trabalhadas é: {soma} h \nA média de horas foi de: {media:.0f} h")