#contato = (nome, telefone, e-mail)
#dicionario será para busca pelo nome
def adicionar_contato(nome, telefone, email):
    if (nome.strip() and telefone.strip() and email.strip()):
        contato = (nome, telefone, email)
        lista_de_contatos.append(contato)
        #dicionario_de_contatos[nome.lower()] = contato
        dicionario_de_contatos[nome.lower()] = {
            'nome': nome,
            'telefone': telefone,
            'email': email
        }
        return f"O contato {contato} foi adicionado a lista. "
    else:
        return "Você não pode inserir o contato com campos vazios!" 

def listar_contatos():
    return (f"A lista de contatos é: {lista_de_contatos}")

def buscar_contato(nome):
    nome = nome.lower()
    if (nome in dicionario_de_contatos):
        contato = dicionario_de_contatos[nome]

        return f"Contato encontrado! {contato} \n| Nome: {contato['nome']}, \n| Telefone: {contato['telefone']} \n| E-mail: {contato['email']} "
    else:
        return "Contato não encontrado."

def atualizar_contato(nome, novo_nome, novo_tel, novo_email):
    busca = buscar_contato(nome)

    if (busca != "Contato não encontrado."):
        #atualiza o dicionario
        dicionario_de_contatos.pop(nome.lower())
        dicionario_de_contatos[novo_nome.lower()] = {
            'nome': novo_nome,
            'telefone': novo_tel,
            'email': novo_email}
        
        #atualiza a lista
        novo_contato = (novo_nome, novo_tel, novo_email)
        for i in range(len(lista_de_contatos)):
            if(lista_de_contatos[i][0] == nome):
                lista_de_contatos[i] = novo_contato
                return f"O elemento foi substituido. \n {lista_de_contatos}"
    else:
        return f"Não foi possível fazer a alteração porque o contato com o nome {nome} não existe."

def excluir_contato(nome):
    busca = buscar_contato(nome)

    if (busca != "Contato não encontrado."):
        #remove do dicionario
        dicionario_de_contatos.pop(nome.lower())
       
        #remove da lista
        for i in range(len(lista_de_contatos)):
            if(lista_de_contatos[i][0] == nome):
                contato_deletado = lista_de_contatos.pop(i)
                return f"O elemento {contato_deletado} foi deletado. \n {lista_de_contatos}"
    else:
        return f"Não foi possível excluir porque o contato com o nome {nome} não existe."

def sair():
    return "Saindo do programa..."


lista_de_contatos = []
dicionario_de_contatos = {}
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
    
    if (opcao == 1):
        nome = input("Digite o nome do novo contato: ")
        telefone = input("Digite o telefone do novo contato: ")
        email = input("Digite o e-mail do novo contato: ")
        print(adicionar_contato(nome, telefone, email))

    elif (opcao == 2):
        print(listar_contatos())
        #print(dicionario_de_contatos.items())

    elif (opcao == 3):
        nome = input("Digite o nome do contato a ser atualizado: ")
        busca = buscar_contato(nome)
        if (busca != "Contato não encontrado."):
            novo_nome = input("Digite o novo nome: ")
            novo_tel = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            print(atualizar_contato(nome, novo_nome, novo_tel, novo_email))
        else:
            print (f"Não foi possível excluir porque o contato com o nome {nome} não existe.")

    elif (opcao == 4):
        nome = input("Digite o nome do contato a ser deletado: ")
        print(excluir_contato(nome))

    elif (opcao == 5):
        nome = input("Insira o nome que você deseja buscar: ")
        print(buscar_contato(nome))

    elif (opcao == 0):
        print(sair())

    else:
        print("Opção inválida.")