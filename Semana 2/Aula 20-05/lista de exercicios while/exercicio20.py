while True:
    senha = input("Digite a senha: ")
    confirma = input("Confirme a senha: ")
    if senha == confirma:
        print("Senha confirmada com sucesso!")
        break
    else:
        print("As senhas não coincidem. Tente novamente.")
