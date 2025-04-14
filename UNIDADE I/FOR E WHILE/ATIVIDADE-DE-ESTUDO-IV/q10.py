confirmacao = 1
operacao = 0
calculo = 0
while confirmacao == 1:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operacao = int(input("1 = Adição \n2 = Subtração \n3 = Multiplicação \n4 = Dvisão \nInforme a operação correspondente: "))
    if (operacao == 1):
        calculo = num1 + num2
        print(f"Soma: {calculo}")
    elif (operacao == 2):
        calculo = num1 - num2
        print(f"Subtração: {calculo}")
    elif (operacao == 3):
        calculo = num1 * num2
        print(f"Multiplicação: {calculo}")
    elif (operacao == 4 and num2 != 0):
        calculo =  num1 / num2
        print(f"Divisão: {calculo}")
    else:
        print("Operação inválida!")
    
    confirmacao = int(input("\nATENÇÃO! \nVocê deseja realizar outra operação? \n1 = 'Sim' \n2 = 'Não' \nInforme: "))