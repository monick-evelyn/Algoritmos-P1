saldo = float(input("Digite seu saldo (R$): "))

if saldo >= 50.00:
    print("Bife com batata frita")
elif saldo >= 20.00 and saldo < 50.00:
    print("Macarrão com molho")
elif saldo >= 10.00 and saldo < 20.00:
    print("Sanduíche com presunto")
else:
    print("Bolacha de água e sal")