import os  # Biblioteca usada para limpar a tela (compatível com Windows e Unix)

# Lista principal para armazenar os alunos
alunos = []

# 🔹 Módulo 1 – Entrada e Armazenamento de Dados
def cadastrar_aluno():
    # Solicita nome e idade do aluno
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")

    # Pergunta quantas notas deseja cadastrar, com validação
    while True:
        try:
            quantidade_notas = int(input("Quantas notas deseja cadastrar? "))
            if quantidade_notas > 0:
                break
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

    # Loop para cadastrar as notas com validação (valores entre 0 e 10)
    notas = []
    for i in range(quantidade_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Valor inválido! Digite um número.")

    # Cria um dicionário com os dados do aluno
    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': notas
    }

    # Adiciona o aluno à lista principal
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

# 🔹 Função auxiliar para calcular média e status (Aprovado ou Reprovado)
def calcular_media_e_status(notas):
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 6 else "Reprovado"
    return media, status

# 🔹 Módulo 2 – Análise de Dados e Condicionais
def listar_alunos():
    if not alunos:  # Verifica se há alunos cadastrados
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        exibir_aluno(aluno)  # Exibe cada aluno formatado

def exibir_aprovados():
    encontrados = False
    for aluno in alunos:
        media, status = calcular_media_e_status(aluno['notas'])
        if status == "Aprovado":
            exibir_aluno(aluno)
            encontrados = True
    if not encontrados:
        print("Nenhum aluno aprovado encontrado.")

def exibir_reprovados():
    encontrados = False
    for aluno in alunos:
        media, status = calcular_media_e_status(aluno['notas'])
        if status == "Reprovado":
            exibir_aluno(aluno)
            encontrados = True
    if not encontrados:
        print("Nenhum aluno reprovado encontrado.")

# 🔹 Função auxiliar para exibir aluno formatado na tela
def exibir_aluno(aluno):
    media, status = calcular_media_e_status(aluno['notas'])
    print(f"""
Nome: {aluno['nome']}
Idade: {aluno['idade']}
Notas: {aluno['notas']}
Média: {media:.2f}
Status: {status}
------------------------""")

# 🔹 Módulo 3 – Busca e Manipulação de Strings
def buscar_aluno_por_nome():
    termo = input("Digite o nome ou parte do nome para buscar: ").lower()
    encontrados = [aluno for aluno in alunos if termo in aluno['nome'].lower()]
    if encontrados:
        for aluno in encontrados:
            exibir_aluno(aluno)
    else:
        print("Nenhum aluno encontrado com esse nome.")

# 🔹 Módulo 4 – Edição e Exclusão de Dados
def editar_cadastro():
    termo = input("Digite o nome do aluno que deseja editar: ").lower()
    for aluno in alunos:
        if termo in aluno['nome'].lower():
            print("Aluno encontrado:")
            exibir_aluno(aluno)

            # Menu de edição
            print("O que deseja editar?")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Notas")
            opcao = input("Escolha uma opção: ")

            # Processa a opção escolhida
            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                aluno['nome'] = novo_nome
            elif opcao == "2":
                nova_idade = input("Digite a nova idade: ")
                aluno['idade'] = nova_idade
            elif opcao == "3":
                # Repete o mesmo processo de cadastro de notas
                while True:
                    try:
                        quantidade_notas = int(input("Quantas notas deseja cadastrar? "))
                        if quantidade_notas > 0:
                            break
                        else:
                            print("Digite um número maior que zero.")
                    except ValueError:
                        print("Valor inválido! Digite um número inteiro.")

                novas_notas = []
                for i in range(quantidade_notas):
                    while True:
                        try:
                            nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
                            if 0 <= nota <= 10:
                                novas_notas.append(nota)
                                break
                            else:
                                print("Nota inválida! Digite um valor entre 0 e 10.")
                        except ValueError:
                            print("Valor inválido! Digite um número.")
                aluno['notas'] = novas_notas
            else:
                print("Opção inválida!")
            print("Cadastro atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def excluir_cadastro():
    termo = input("Digite o nome do aluno que deseja excluir: ").lower()
    for aluno in alunos:
        if termo in aluno['nome'].lower():
            print("Aluno encontrado:")
            exibir_aluno(aluno)
            confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()
            if confirmacao == 's':
                alunos.remove(aluno)
                print("Aluno excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Aluno não encontrado.")

# 🔹 Módulo 5 – Menu Principal e Integração
def limpar_tela():
    # Limpa a tela de forma compatível com Windows ('cls') ou Linux/Mac ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    while True:
        # Exibe as opções do menu
        print("""
===== MENU =====
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno por nome
4 - Exibir aprovados
5 - Exibir reprovados
6 - Editar cadastro
7 - Excluir cadastro
0 - Sair
================
""")
        opcao = input("Escolha uma opção: ")

        # Chama as funções de acordo com a opção escolhida
        if opcao == "1":
            limpar_tela()
            cadastrar_aluno()
        elif opcao == "2":
            limpar_tela()
            listar_alunos()
        elif opcao == "3":
            limpar_tela()
            buscar_aluno_por_nome()
        elif opcao == "4":
            limpar_tela()
            exibir_aprovados()
        elif opcao == "5":
            limpar_tela()
            exibir_reprovados()
        elif opcao == "6":
            limpar_tela()
            editar_cadastro()
        elif opcao == "7":
            limpar_tela()
            excluir_cadastro()
        elif opcao == "0":
            limpar_tela()  # Limpa a tela antes de sair
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# 🔸 Executa o menu ao iniciar o programa
mostrar_menu()
