nota = float(input("Digite sua nota: "))

if nota < 0:
     print("Nota inválida, ela deve ser positiva")
elif nota >= 7:
    print(f"Você tirou {nota} na sua nota e está aprovado")
elif nota < 7:
     print(f"Você tirou {nota} na sua nota e está reprovado")
else:
     print("ocorreu um erro")