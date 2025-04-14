contador = 0
termo_1 = 1
termo_2 = 1
print(f"1° termo: {termo_1}")
print(f"2° termo: {termo_2}")
for i in range(8):
    termo_3 = termo_1 + termo_2
    print(f"{i + 1}° termo: {termo_3}")
    termo_1 = termo_2
    termo_2 = termo_3