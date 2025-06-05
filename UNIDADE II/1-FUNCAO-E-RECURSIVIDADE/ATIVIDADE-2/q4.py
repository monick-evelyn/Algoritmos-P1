def somadigitos (num):
    soma = 0
    if (num >= 0 and num < 10):
        return num
    elif (num < 0 and num > -10):
        return num * -1
    else:
        if (num < 0):
            num = num * -1
        soma = num%10 + somadigitos(num//10)
        return soma
print(somadigitos(89))