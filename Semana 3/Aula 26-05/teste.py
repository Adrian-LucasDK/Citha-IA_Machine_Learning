import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Funções auxiliares
# -------------------------------

def prever(x, intercepto, inclinacao):
    """Calcula a predição baseada na equação da reta."""
    return intercepto + inclinacao * x

def custo(intercepto, inclinacao, X, Y):
    """Calcula o erro quadrático médio (função de custo)."""
    y_previsto = prever(X, intercepto, inclinacao)
    return np.mean((y_previsto - Y) ** 2) / 2

def plotar_regressao(X, Y, intercepto, inclinacao):
    """Plota os dados e a reta de regressão."""
    plt.figure(figsize=(8, 5))
    plt.scatter(X, Y, color='green', label='Dados reais')
    plt.plot(X, prever(X, intercepto, inclinacao), color='orange', label='Reta de regressão')
    plt.xlabel('Horas de Sol por Dia')
    plt.ylabel('Produção de Frutas (kg)')
    plt.title('Regressão Linear: Produção vs Horas de Sol')
    plt.legend()
    plt.grid(True)
    plt.show()

def plotar_custo(historia_custo):
    """Plota a evolução da função de custo."""
    plt.figure(figsize=(8, 5))
    plt.plot(historia_custo, color='blue')
    plt.xlabel('Épocas')
    plt.ylabel('Custo')
    plt.title('Convergência da Função de Custo')
    plt.grid(True)
    plt.show()

# -------------------------------
# Dados de entrada
# -------------------------------

# Exemplo de dados: Horas de sol (X) e Produção de frutas (Y)
X = np.array([4, 5, 6, 7, 8], dtype=float)
Y = np.array([40, 45, 54, 56, 62], dtype=float)

# Hiperparâmetros
taxa_aprendizado = 0.01   # taxa de aprendizado
epocas = 10  # número de iterações

# Inicialização dos parâmetros
intercepto = 0.0
inclinacao = 0.0
historia_custo = []

# -------------------------------
# Gradiente Descendente
# -------------------------------

for _ in range(epocas):
    y_previsto = prever(X, intercepto, inclinacao)
    erro = y_previsto - Y
    grad0 = np.mean(erro)
    grad1 = np.mean(erro * X)
    intercepto -= taxa_aprendizado * grad0
    inclinacao -= taxa_aprendizado * grad1
    historia_custo.append(custo(intercepto, inclinacao, X, Y))

# -------------------------------
# Resultados
# -------------------------------

print(f"Intercepto (theta0): {intercepto:.2f} \n\tEste valor representa o ponto onde a reta cruza o eixo y.")
print(f"\nInclinação (theta1): {inclinacao:.2f} \n\tA inclinação da reta indica a taxa de variação da produção de frutas\n\tem relação às horas de sol.")
print(f"\nCusto final: {historia_custo[-1]:.2f} \n\tEste é o valor da função de custo final, que mede o erro médio \n\tentre as previsões e os valores reais.")

# Previsão para 6.5 horas de sol
x_teste = 6.5
y_previsto = prever(x_teste, intercepto, inclinacao)
print(f"\n\tOu seja, para {x_teste} horas de sol, a produção estimada é {y_previsto:.2f} kg\n\tIsso mostra como a nossa equação de regressão prevê a produção de frutas\n\tcom base nas horas de sol.")

# -------------------------------
# Visualizações
# -------------------------------

plotar_regressao(X, Y, intercepto, inclinacao)
plotar_custo(historia_custo)
        