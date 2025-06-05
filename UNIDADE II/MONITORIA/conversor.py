def conversor (segundos):
    horas = segundos//3600
    minutos = (segundos % 3600) // 60
    segundos_real = segundos - (minutos * 60 + horas * 3600) 
    return f"{horas:02} horas {minutos:02} minutos e {segundos_real:02} segundos."

print(conversor(int(input())))