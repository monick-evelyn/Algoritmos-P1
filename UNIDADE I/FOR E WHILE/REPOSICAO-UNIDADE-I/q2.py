import random

numero = random.randint(1, 100)
print(numero)
tentativas = 0
while tentativas < 10:
    if(tentativas < 10):
        palpite = int(input(f"Informe o {tentativas + 1}° palpite sobre o número sorteado: "))
        tentativas += 1
        if (palpite < numero):
            print("Muito baixo.")
        elif(palpite > numero):
            print("Muito alto")
        else:
            print("Palpite correto!")
            break
if (tentativas >= 10 and palpite != numero):
    print("Tentitivas esgotadas!")
