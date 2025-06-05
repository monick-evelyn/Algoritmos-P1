def multiplicacao (a, b):
    if (b == 0):
        return 0
    elif (b == 1):
        return a
    else:
        return a + multiplicacao(a, (b - 1))
print(multiplicacao(2, 4))