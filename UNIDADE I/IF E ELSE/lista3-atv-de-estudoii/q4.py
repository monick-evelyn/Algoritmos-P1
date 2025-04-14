lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

#Tem que verificar se é um triângulo
if(lado1 + lado2 > lado3 or lado3 + lado2 == lado1 or lado1 + lado3 > lado2):
    #O código verifica se a soma de quaisquer dois lados é sempre maior que o terceiro lado. Isso é conhecido como a inequação triangular, que é uma regra matemática fundamental para garantir que as medidas possam formar um triângulo.

    #lado1 + lado2 > lado3: A soma dos dois primeiros lados precisa ser maior que o terceiro lado.
    #lado2 + lado3 > lado1: A soma dos dois segundos lados precisa ser maior que o primeiro lado.
    #lado1 + lado3 > lado2: A soma dos dois últimos lados precisa ser maior que o segundo lado.
    if (lado1 == lado2 == lado3):
        print("o triângulo é equilatéro")
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("o triângulo é isósceles")
    else:
        print("o triângulo é escaleno")
else:
    print("As medidas dos lados não formam um triângulo")