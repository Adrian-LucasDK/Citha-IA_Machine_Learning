agenda = {'Maria': '9922-4455', 'João': '9888-3322'}

nome = input("Digite o nome que deseja remover: ")

if nome in agenda:
    confirmar = input(f"Tem certeza que quer remover {nome}? (s/n): ").lower()
    if confirmar == 's':
        # Pode usar del ou pop
        agenda.pop(nome)
        print(f"{nome} foi removido da agenda.")
    else:
        print("Remoção cancelada.")
else:
    print(f"{nome} não está na agenda.")

print("Agenda atualizada:", agenda)
