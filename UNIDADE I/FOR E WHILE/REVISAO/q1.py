n = int(input("Digite qual tabuada (de 1 a 10): "))
for i in range (1, 11, 1):
    if i % 2 == 0:
        print(f"Maria: {i} x {n} = {i*n}")
    else:
        print(f"João: {i} x {n} = {i*n}")