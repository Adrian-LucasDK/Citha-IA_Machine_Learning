preço = float (input("Digite o preço do produto em R$: "))
desc = float (input("Digite o desconto do produto em %: "))

pf = preço - (preço*desc/100)

print (f"O preço final com desconto é igual: R${pf}")