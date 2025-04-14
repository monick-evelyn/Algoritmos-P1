salario = 0.0
soma_salario = 0
soma_filhos = 0
contador = 0
maior_salario = 0

while(salario != -1):
    salario = float(input("Informe um salário (digite -1 para parar): "))
    if (salario != -1):
        filhos = int(input("Informe o número de filhos: "))
        soma_salario += salario
        soma_filhos += filhos
        contador = contador + 1

        if (salario > maior_salario):
            maior_salario = salario
print(f"Média dos salários: R$ {soma_salario/contador:.2f}")
print(f"Média de filhos: R$ {soma_filhos//contador}")
print(f"Maior salário: R$ {maior_salario:.2f}")