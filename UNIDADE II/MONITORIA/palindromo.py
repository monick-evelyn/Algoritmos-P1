#palindromo recursivo
#ARARA
def palindromo (palavra):
    if (len(palavra) == 1):
        return True
    elif (palavra[0] != palavra[-1]): #critério de parada 
        return False
    else:
        return palindromo(palavra[1:-1])
palavra = "arara"
print(palavra[1:-1])
print(palindromo("arara"))
print(palindromo("jucelio"))
print(palindromo("natan"))