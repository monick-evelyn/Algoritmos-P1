idade = 0
horas = 0
contador_func = 0
soma_horas = soma_idade = idade_maior = 0
while idade != -1:
    idade = int(input("Informe a idade: "))
    if (idade != -1):
        horas = int(input("Informe as horas trabalhadas: "))
        soma_horas += horas
        soma_idade += idade
        contador_func += 1
        if (idade > idade_maior):
            idade_maior = idade
media_horas = soma_horas / contador_func
media_idade = soma_idade // contador_func
print(f"\nRESULTADOS\n| Média das idades dos funcionários: {media_idade}\n| Média de horas trabalhadas: {media_horas:.1f}\n| Idade mais alta: {idade_maior}")