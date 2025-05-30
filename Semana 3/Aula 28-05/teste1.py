import numpy as np  # álgebra linear
import pandas as pd  # processamento de dados, leitura de CSV
import matplotlib.pyplot as plt

# Caminho local do arquivo CSV na sua máquina Windows
caminho_arquivo = r"C:\Users\adria\Videos\Citha-IA_Machine_Learning\Semana 3\Aula 28-05\global_street_food.csv"

# Leitura do dataset usando o caminho local
df = pd.read_csv(caminho_arquivo)

# Contar quantos registros existem por país
ulkeler = df['Country'].value_counts()

# Mostrar as primeiras linhas do dataset filtrado para 'Turkey' (Turquia)
print(df[df['Country'] == 'Turkey'])

# Ver os valores e índices para gráficos
print(ulkeler.values)
print(ulkeler.index)

# Gráfico de pizza da distribuição de países
plt.figure(figsize=(16, 16))
plt.pie(ulkeler.values, labels=ulkeler.index, autopct="%1.1f%%")
plt.show()

# Filtrar somente entradas da Turquia para outro gráfico
TR = df[df['Country'] == 'Turkey']

# (Aqui seu código termina, você pode continuar seu gráfico ou análise)
plt.figure(figsize=(10, 10))
