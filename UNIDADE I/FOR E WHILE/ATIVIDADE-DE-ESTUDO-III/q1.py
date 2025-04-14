divisores = 0
for i in range (1, 201, 1):
    if (i % 3 == 0 and i % 5 == 0):
        divisores = divisores + 1
print (f"Divisores de 3 e 5: {divisores}")