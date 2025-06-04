def fatorial (num):
    if (num < 0):
        return "Inválido"
    elif (num == 0) or (num == 1):
        return 1
    else:
        return num * fatorial(num - 1)
    
def trailingzerosfatorial(fat):
    fatorial = str(fat)
    return fatorial.count("0")

print(trailingzerosfatorial(fatorial(10)))