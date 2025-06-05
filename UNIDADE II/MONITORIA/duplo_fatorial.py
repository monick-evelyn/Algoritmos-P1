#fatorial duplo

def fatorial_duplo(num):
    if(num % 2 == 0 or num < 0):
        return "Inválido"
    elif (num == 1):
        return 1
    else:
        return num * fatorial_duplo(num - 2)
    
print(fatorial_duplo(5))