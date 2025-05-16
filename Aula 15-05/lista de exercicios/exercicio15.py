temp = float(input("Digite a temperatura em graus C°: "))

if temp < 15:
    print(f"A temperatura de {temp}C° indica que está um clima frio")
elif temp >= 15 and temp <= 25:
    print(f"A temperatura de {temp}C° indica que está um clima moderado")
elif temp > 25:
    print(f"A temperatura de {temp}C° indica que está um clima quente")
else:
    print("Ocorreu um erro")