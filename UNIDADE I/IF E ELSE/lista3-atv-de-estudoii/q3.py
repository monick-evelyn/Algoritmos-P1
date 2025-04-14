ano = int(input("Digite um ano: "))
# 1930 - 1934 - 1938 - 1942 - 1946 - 1950
ANO_INICIO = 1930

if ano >= 1930 and (ano - 1930) % 4 == 0:
    ##Verifca se é múltiplo de 4 contando a partir de 1930
    print (f"{ano} é ano de copa")
else:
    print (f"{ano} não é ano de copa")