opcao = ''

while opcao != '0':
    print("\nMenu:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu a opção 1.")
    elif opcao == '2':
        print("Você escolheu a opção 2.")
    elif opcao == '3':
        print("Você escolheu a opção 3.")
    elif opcao == '0':
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")
