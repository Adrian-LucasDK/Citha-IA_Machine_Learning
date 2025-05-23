def usuario():
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu cpf: "))
    email = input("Digite seu email: ")
    time = input("Digite seu time: ")
    print (f"Usuário Cadastrado com Sucesso \nNome: {nome} \nCPF: {cpf} \nEmail: {email} \nTime: {time}")

def media():
    notas = []
    
    quantidade = int(input("Quantas notas você quer adicionar? "))
    
    contador = 0
    while contador < quantidade:
        nota = float(input(f"Digite a {contador + 1}ª nota: "))
        notas.append(nota)
        contador += 1
    
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.1f}")

    if media >= 7:
        print("Parabéns você foi Aprovado")
    else:
        print("Você foi Reprovado")
  
media()
