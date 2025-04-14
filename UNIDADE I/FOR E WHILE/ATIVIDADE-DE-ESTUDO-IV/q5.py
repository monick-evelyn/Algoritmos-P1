nome = ""
largura = 0.0
soma = 0.0
area = 0.0
comprimento = 0.0
while nome != "FIM":
    nome = str(input("Informe um nome pro cômodo (FIM para parar): ")).upper()
    if (nome != "FIM"):
        largura = float(input("Informe a largura em metros: "))
        comprimento = float(input("Informe o comprimento em metros: "))
        area = largura * comprimento
        #print(f"Área do {nome}: {area} m2")
        soma += area
        #print(f"Soma das áreas: {soma}")
print (f"A soma das áreas é: {soma}")