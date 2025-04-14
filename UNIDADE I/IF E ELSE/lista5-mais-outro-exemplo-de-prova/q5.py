salario = float(input("Informe o salário do funcionário: "))

if (salario <= 2000.0):
    print("Insento")
elif (salario >= 2001.0 and salario <= 5000.0):
    print("Imposto de 10%")
else: 
    print("Imposto de 20%")