horas_semanais = int(input("Informe o número de horas semanais de exercício: "))

if(horas_semanais < 2):
    print("Iniciante")
elif(horas_semanais >= 2 and horas_semanais <= 5):
    print("Regular")
else:
    print("Atleta")