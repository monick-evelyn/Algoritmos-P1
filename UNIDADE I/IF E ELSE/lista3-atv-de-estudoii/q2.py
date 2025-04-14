#Critério: Menor preço e maior rendimento
preco_gasolina = float(input("Insira o preço da gasolina: ")) ## 6.00
consumo_gasolina = float(input("Informe o consumo médio do carro com gasolina (Km/L): "))

preco_etanol = float(input("Insira o preço do etanol: "))
consumo_etanol = float(input("Informe o consumo médio do carro com etanol (Km/L): "))

#preco = 1L 
#consumo = 1l / Km

resultado_gasolina = preco_gasolina / consumo_gasolina
resultado_etanol = preco_etanol / consumo_etanol

if (resultado_etanol < resultado_gasolina):
    print(f"O mais vantajoso é comprar etanol {resultado_etanol}")
elif (resultado_gasolina < resultado_etanol):
    print(f"O mais vantajoso é comprar gasolina {resultado_gasolina}")
else:
    print("Tanto faz") 
    ##Considerar o 3° caso onde os dois se igualam