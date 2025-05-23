preço_uni = float(input("Digite o preço unitário do produto em R$: "))
quant = float(input("Digite a quantidades de produtos que você pegou: "))

custo = preço_uni*quant

print(f"O custo total de todos os produtos que você comprou é igual a: R${custo:.2f}")
