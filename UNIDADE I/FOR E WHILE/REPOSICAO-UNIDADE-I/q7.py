altura = 2
sobe = 1
desce = 0.5
percurso = 0
dias = 0
while percurso < altura:
    percurso += sobe
    if (percurso < altura):
        percurso -= desce
    dias += 1
print(f"Ela demora {dias} dias")