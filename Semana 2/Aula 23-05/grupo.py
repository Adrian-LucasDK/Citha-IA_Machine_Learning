# ===============================
# 🧩 MÓDULO 0 – IMPORTAÇÕES E LISTAS
# ===============================

import os

# Lista principal para armazenar os alunos
alunos = []


# ===============================
# 🧩 MÓDULO 1 – ENTRADA E ARMAZENAMENTO DE DADOS
# ===============================

def cadastrar_aluno():
    limpar_tela()
    print("=== Cadastro de Aluno ===")

    aluno = {}  # Dicionário para os dados do aluno

    aluno['nome'] = input("Informe o nome do aluno: ")

    while True:
        idade = input("Informe a idade do aluno: ")
        if idade.isdigit():
            aluno['idade'] = int(idade)
            break
        else:
            print("Idade inválida! Digite um número inteiro.")

    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Informe a nota {i} (entre 0 e 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Nota inválida! Digite um número decimal.")

    aluno['notas'] = notas
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")


# ===============================
# 🧩 MÓDULO 2 – ANÁLISE DE DADOS E CONDICIONAIS
# ===============================

def listar_alunos():
    limpar_tela()
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        exibir_aluno(aluno)


def exibir_aluno(aluno):
    media = sum(aluno['notas']) / len(aluno['notas'])
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    print(f"Nome : {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)


def exibir_aprovados():
    limpar_tela()
    print("\n--- Alunos Aprovados ---")
    encontrados = False
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if media >= 6:
            exibir_aluno(aluno)
            encontrados = True
    if not encontrados:
        print("Nenhum aluno aprovado.")


def exibir_reprovados():
    limpar_tela()
    print("\n--- Alunos Reprovados ---")
    encontrados = False
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if media < 6:
            exibir_aluno(aluno)
            encontrados = True
    if not encontrados:
        print("Nenhum aluno reprovado.")


# ===============================
# 🧩 MÓDULO 3 – BUSCA E MANIPULAÇÃO DE STRINGS
# ===============================

def buscar_aluno_por_nome():
    limpar_tela()
    termo = input("Digite o nome ou parte do nome do aluno para buscar: ").lower()
    encontrados = []

    for aluno in alunos:
        if termo in aluno['nome'].lower():
            encontrados.append(aluno)

    if encontrados:
        print("\n--- Alunos Encontrados ---")
        for aluno in encontrados:
            exibir_aluno(aluno)
    else:
        print("Nenhum aluno encontrado com esse nome.")


# ===============================
# 🧩 MÓDULO 4 – EDIÇÃO E EXCLUSÃO DE DADOS
# ===============================

def editar_cadastro():
    limpar_tela()
    termo = input("Digite o nome do aluno que deseja editar: ").lower()
    for aluno in alunos:
        if termo in aluno['nome'].lower():
            print("Aluno encontrado:")
            exibir_aluno(aluno)

            print("O que deseja editar?")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Notas")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                aluno['nome'] = novo_nome
            elif opcao == "2":
                while True:
                    nova_idade = input("Digite a nova idade: ")
                    if nova_idade.isdigit():
                        aluno['idade'] = int(nova_idade)
                        break
                    else:
                        print("Idade inválida. Digite um número inteiro.")
            elif opcao == "3":
                novas_notas = []
                for i in range(1, 4):
                    while True:
                        try:
                            nota = float(input(f"Digite a nota {i} (0 a 10): "))
                            if 0 <= nota <= 10:
                                novas_notas.append(nota)
                                break
                            else:
                                print("Nota inválida! Digite um valor entre 0 e 10.")
                        except ValueError:
                            print("Valor inválido! Digite um número decimal.")
                aluno['notas'] = novas_notas
            else:
                print("Opção inválida!")

            print("Cadastro atualizado com sucesso!")
            return

    print("Aluno não encontrado.")


def excluir_cadastro():
    limpar_tela()
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


# ===============================
# 🧩 MÓDULO 5 – MENU PRINCIPAL E INTEGRAÇÃO
# ===============================

def mostrar_menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno por nome")
        print("4 - Exibir aprovados")
        print("5 - Exibir reprovados")
        print("6 - Editar cadastro")
        print("7 - Excluir cadastro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        elif opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno_por_nome()
        elif opcao == "4":
            exibir_aprovados()
        elif opcao == "5":
            exibir_reprovados()
        elif opcao == "6":
            editar_cadastro()
        elif opcao == "7":
            excluir_cadastro()
        else:
            print("Opção inválida. Tente novamente.")


# 🔹 Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# 🔸 Inicia o programa chamando o menu principal
mostrar_menu()
