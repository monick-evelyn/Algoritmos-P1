def verificar_primo(num):
    contador = 0
    if num < 1:
        return False
    else:
        for i in range (num, 1, -1):
            if 10 % i == 0:
                contador += 1
        if contador == 2:
            return True
        else:
            return False
print(verificar_primo(10))
print(verificar_primo(7))