x = float(input("Digite o número de X: "))
y = float(input("Digite o número de y: "))

if x == 0 and y == 0:
    print(f"os ponto {x} e {y} estão na origem")
elif x > 0 and y > 0:
    print(f"os ponto {x} e {y} estão na quadrante Q1")
elif x < 0 and y > 0:
    print(f"os ponto {x} e {y} estão na quadrante Q2")
elif x < 0 and y < 0:
    print(f"os ponto {x} e {y} estão na quadrante Q3")
elif x > 0 and y < 0:
    print(f"os ponto {x} e {y} estão na quadrante Q4")
elif x != 0 and y == 0:
    print(f"os ponto {x} e {y} estão no eixo x")
elif x == 0 and y != 0:
    print(f"os ponto {x} e {y} estão no eixo y")
else:
    print("O código deu erro")