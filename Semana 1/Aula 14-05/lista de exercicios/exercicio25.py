n1 = int(input("Digite a primeira nota: "))
p1 = int(input("Digite o peso da primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
p2 = int(input("Digite o peso da segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
p3 = int(input("Digite o peso da terceira nota: "))

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f"O valor da média ponderada das notas {n1},{n2} e {n3} com os pesos {p1},{p2} e {p3} respectivamente é igual: {media:.2f}")