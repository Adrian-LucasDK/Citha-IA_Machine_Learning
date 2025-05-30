import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Dados originais
X = np.array([[10], [20], [30], [40], [50]])

# Min-Max Normalization
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)

# Mean Normalization (manual)
X_mean = X.mean()
X_min = X.min()
X_max = X.max()
X_meannorm = (X - X_mean) / (X_max - X_min)

# Z-Score Standardization
scaler_zscore = StandardScaler()
X_zscore = scaler_zscore.fit_transform(X)

# Plotando os resultados
plt.figure(figsize=(10, 6))

plt.plot(X, np.zeros_like(X), 'o', label='Original', markersize=10)
plt.plot(X, X_minmax, 'o-', label='Min-Max [0, 1]')
plt.plot(X, X_meannorm, 's--', label='Mean Normalization')
plt.plot(X, X_zscore, 'd-.', label='Z-Score')

plt.title('Comparação de Técnicas de Normalização/Padronização')
plt.xlabel('Valor Original')
plt.ylabel('Valor Transformado')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()