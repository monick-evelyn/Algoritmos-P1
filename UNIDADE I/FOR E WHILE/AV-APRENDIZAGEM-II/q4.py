n = int(input("Informe um número: "))
termo1 = 0
termo2 = 1
soma = termo1 + termo2
print(f"{termo1} + {termo2} = {soma}")
for i in range(n + 1):
    termo1 = termo2
    termo2 = soma
    soma = termo1 + termo2
    print(f"{termo1} + {termo2} = {soma}")