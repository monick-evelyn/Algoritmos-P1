def convertertempo(minutos):
    horas = minutos // 60
    minutos_convert = minutos - (horas * 60)
    return (f"{horas} horas e {minutos_convert} minutos")
print(convertertempo(150))