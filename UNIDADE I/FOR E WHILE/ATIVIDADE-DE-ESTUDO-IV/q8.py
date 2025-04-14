nota = 0
contador = 0
soma_nota = 0
maior_nota = 0
soma_disciplinas = 0
#enquanto a nota for positiva
while nota >= 0:
    nota = float(input("Informe a nota: "))
    #mesma verificação
    if (nota >= 0):
        contador += 1
        soma_nota += nota #soma das notas
        disciplina = int(input("Digite o número de disciplinas: ")) #disciplina
        soma_disciplinas += disciplina
        if (nota > maior_nota):
            maior_nota = nota
media_nota = soma_nota / contador
media_disciplinas = soma_disciplinas // contador
print(f"A média das notas do aluno é de: {media_nota:.1f} \nA média do número de disciplinas é de: {media_disciplinas} \nMaior nota: {maior_nota}")