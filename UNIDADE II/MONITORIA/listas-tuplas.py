def separar_par_e_impar(lista_de_num):
    pares = []
    impares = []
    tupla_de_numeros = (pares, impares)
    for num in lista_de_num:
        if (eh_par(num) == True):
            pares.append(num)
        else:
            impares.append(num)
    return tupla_de_numeros


def eh_par(num):
    if (num % 2 == 0):
        return True
    else:
        return False

numeros = [1,2,3,4,5]
print(separar_par_e_impar(numeros))
