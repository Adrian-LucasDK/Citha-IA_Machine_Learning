print("Bem Vindo(a) ao Sistema")
print("-----------------------")
sel = int(input(f"Utilize os números para selecionar uma das opções do menu abaixo:\n"
      f"1 - Cadastrar\n"
      f"2 - Consultar\n"
      f"3 - Atualizar\n" 
      f"4 - Excluir\n"))

match sel:
    case 1:
        print("O que você quer cadastrar?")
    case 2:
        print("O que você quer consultar?")
    case 3:
        print("O que você quer atualizar?")
    case 4:
        print("O que você quer excluir?")
    case 5:
        print("Operação Inválida! Digite número de 1 a 4")