nome_correto = "monibraba"
senha_correta = "moni123"

nome = str(input("Digite o nome: "))
senha = str(input("Digite a senha: "))

if nome == nome_correto and senha == senha_correta:
    print("Login bem-sucedido")
else:
    print("Login inválido")