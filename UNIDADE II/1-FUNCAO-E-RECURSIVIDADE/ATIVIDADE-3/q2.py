'''
def contarocorrencias(s, c):
    return s.count(c)
print(contarocorrencias("Booom dia", "o"))
'''
# Crie uma função recursiva que conte o número de ocorrencias em uma lista; Ex: Entrada([1,2,2,3,2],2) saida:3
def contarocorrencias(s, c):
    contador = 0 
    if (len(s) < 1):
        return contador
    else:
        if s[0] == c:
            contador += 1
        return contador + contarocorrencias(s[1:], c)

print(contarocorrencias([1,2,2,3,2],2))    
print(contarocorrencias("Boom dia","o"))  