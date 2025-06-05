#exibir_bem_vindo: "Bem vindo"; exibir_creditos: "Desenvolvido por [Seu nome]; sair: "Saindo do programa..."; menu(3): "Saindo do programa..." tipo assim

def creditos():
    return "By monick"

def bem_vindo():
    return "Bem-vindo!"

def sair():
    return "Saindo"

def menu(entrada):
    if (entrada == 1):
        return (bem_vindo())
    elif (entrada == 2):
        return (creditos())
    elif(entrada == 3):
        return(sair())
    else:
        return "inválida"

op = int(input("Digite: "))
print(menu(op))
while (op != 3):
    print(menu(op))
    op = int(input("Digite: "))