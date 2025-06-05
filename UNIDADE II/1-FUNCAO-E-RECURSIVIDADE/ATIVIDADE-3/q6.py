def somatorio_quadrados (n):
    if (n < 1):
        return "Inválido"
    elif (n == 1):
        return 1
    else:
        return n**2 + somatorio_quadrados(n - 1)
print(somatorio_quadrados(3))