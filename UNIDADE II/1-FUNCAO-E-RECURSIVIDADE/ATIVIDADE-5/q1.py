def calculadora_simples(num1, num2, op):
    if (op == 1):
        return num1 + num2
    elif (op == 2):
        return num1 - num2
    elif (op == 3):
        return num1 * num2
    elif (op == 4):
        return num1 / num2
    else:
        return("Operação inválida")
    
print(calculadora_simples(2, 2, 4))