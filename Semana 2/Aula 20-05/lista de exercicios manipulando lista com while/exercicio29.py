itens = []

while True:
    print("\nMenu:")
    print("1) Adicionar item")
    print("2) Listar itens")
    print("3) Remover item")
    print("4) Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        item = input("Digite o item para adicionar: ")
        itens.append(item)
        print(f"Item '{item}' adicionado.")

    elif escolha == '2':
        if itens:
            print("Itens na lista:")
            for i, item in enumerate(itens, start=1):
                print(f"{i}. {item}")
        else:
            print("A lista está vazia.")

    elif escolha == '3':
        if itens:
            item_remover = input("Digite o item para remover: ")
            if item_remover in itens:
                itens.remove(item_remover)
                print(f"Item '{item_remover}' removido.")
            else:
                print("Item não encontrado na lista.")
        else:
            print("A lista está vazia.")

    elif escolha == '4':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
