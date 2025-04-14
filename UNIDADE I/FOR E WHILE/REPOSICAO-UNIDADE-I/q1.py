altura = int(input("Informe a altura da pirâmide: "))
for i in range(1, altura + 1): #vai de 1 a altura
    print(" "*(altura - i) + (2*i-1)*"*")

for i in range(altura, 0, -1):
    print(" "*(altura - i) + (2*i-1)*"*")