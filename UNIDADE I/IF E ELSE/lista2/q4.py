num = int(input("Digite um número: "))

resultado = 0
if (num < 100):
    resultado = num + 100
else:
    resultado = num - 100
    
print(f"O resultado é: {resultado}")