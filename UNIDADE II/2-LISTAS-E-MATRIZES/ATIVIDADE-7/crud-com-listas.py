def adicionar(nome):
    lista.append(nome)
    return "Elemento adicionado"

def deletar(nome):
    if buscar(nome) != "Elemento não encontrado":
        lista.remove(nome)
        return "Elemento removido"
    else:
        return "Elemento não encontrado"

def listar():
    return(lista)

def atualizar(nome, novo_nome):
    indice = lista.index(nome)
    if (indice != -1):
        lista[indice] = novo_nome
        return "Elemento atualizado"
    else:
        return "Elemento não encontrado"
    
def buscar(nome):
    if nome in lista:
        return f"Elemento {nome} está na lista"
    else:
        return "Elemento não encontrado"

def sair():
    return "Saindo do programa..."
lista = []
opcao = 6
while (opcao != 0):
    opcao = int(input((f'''
{"=~"*5} Gerenciador de Contatos {"=~"*5}
1 - Adicionar contato.
2 - Listar contatos.
3 - Atualizar contato.
4 - Excluir contato.
5 - Buscar contato.
0 - Encerrar o programa.
{"=~"*22}
Digite aqui: ''')))
    if opcao == 1:
        nome = input("Digite o novo nome: ")
        print(adicionar(nome))
    elif opcao == 2:
        print(listar())
    elif opcao == 3:
        nome = input("Digite o nome: ")
        if (buscar(nome) != "Elemento não encontrado"):
            novo_nome = input(f"Digite o novo nome de {nome}: ")
            print(atualizar(nome, novo_nome))
        else:
            print("Não encontrado")
    elif opcao == 4:
        nome = input("Nome a ser deletado: ")
        print(deletar(nome))
    elif opcao == 5:
        busca = input("Busca: ")
        print(buscar(busca))
    elif opcao == 0:
        print(sair())
    else:
        print("Opção inválida")