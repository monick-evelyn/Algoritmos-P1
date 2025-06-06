'''def contar_letras(palavra):
    dicionario = {}
    for letra in palavra: #b 
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1 #b = 1
    return dicionario'''
palavra = "banana"
#$print(contar_letras("banana"))

dicionario = {}
for letra in palavra: #b 
    if letra in dicionario:
        dicionario[letra] += 1
        print(f"{letra} {dicionario[letra]}")
    else:
        dicionario[letra] = 1 #b = 1
        print(f"{letra} {dicionario[letra]}")
print(dicionario)