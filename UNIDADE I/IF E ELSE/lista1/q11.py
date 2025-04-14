num = int(input("Digite um número com 3 dígitos: "))
#dividir por 10, o modulo sera o ultimo digito
soma = 0

for i in range(3):
    ultimo_digito = num % 10
    num = num//10
    soma = soma + ultimo_digito

print(f"A soma de cada dígito do número é: {soma}")