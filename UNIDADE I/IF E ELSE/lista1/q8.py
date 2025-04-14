#Crie um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
#Exiba o total em dias.

quant_cigarros_dias = int(input("Quantos cigarros o fumante consome por dia? "))
quant_anos = int(input("Faz quantos anos que ele fuma: "))

tempo_de_vida = (quant_cigarros_dias * quant_anos * 10 * 365) //1440

print(f"Se o fumante consomiu {quant_cigarros_dias} cigarros por dia durante {quant_anos} anos, ele perdeu {tempo_de_vida} minutos de vida")