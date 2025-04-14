max = int(input("Digite o número limite: "))
soma = 0
contador = 0
for i in range (1, max+1): #intervalo de 1 até o numero informado
    for n in range(1, i+1): #intervalo de 1 até o número em i (Ex.: quando i = 3, o intervalo n é de [1, 2, 3])
        if(i % n == 0): #verifica se i é divisil por algum numero de n (Ex.: quando i = 3, 3 % 1 = 0, 3 % 2 == 1, 3 % 3 == 0)
            #print (f"{i} é divisil por {n}")
            contador += 1 #conta apenas os divisiveis até chegar no maximo de n

    if (contador == 2): #quando o laço de n acabar, e i tiver apenas 2 divisores, ele é primo.
        print(f"{i} é primo")
        soma += i #soma dos primos

    contador = 0 #quando o laço termina, zera o contador
print(f"A soma dos números primos entre 1 e {max} é: {soma}")