'''def contar_letras(palavra):
    dicionario = {}
    for letra in palavra: #b 
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1 #b = 1
    return dicionario'''
#$print(contar_letras("banana"))

palavra = "banana"
dicionario = {}
#chave = letra; valor = quant. de ocorrências da letra
for letra in palavra: #b 
    if letra in dicionario:
        dicionario[letra] += 1
        #print(f" {letra} {dicionario[letra]} {dicionario}")
    else:
        dicionario[letra] = 1 #b = 1
        #print(f" {letra} {dicionario[letra]} {dicionario}")
print(dicionario) #{'b': 1, 'a': 3, 'n': 2}