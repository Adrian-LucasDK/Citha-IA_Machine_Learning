import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Gerando dados artificiais
np.random.seed(42)

# Grupo 1: média em (2, 2)
grupo1 = np.random.randn(50, 2) + np.array([2, 2])

# Grupo 2: média em (8, 3)
grupo2 = np.random.randn(50, 2) + np.array([8, 3])

# Grupo 3: média em (4, 7)
grupo3 = np.random.randn(50, 2) + np.array([4, 7])

# Grupo 4: média em (8, 8)
grupo4 = np.random.randn(50, 2) + np.array([8, 8])

# Concatenando todos os grupos em um só array
X = np.vstack([grupo1, grupo2, grupo3, grupo4])

# Aplicando k-means para k=4
k = 4
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# Atribuições finais dos pontos aos clusters
labels = kmeans.labels_

# Coordenadas dos centróides finais
centers = kmeans.cluster_centers_

# Plotando os pontos e os centróides
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='*', s=200, edgecolors='black', c="#40f75c")
plt.title("Agrupamento com k-means (k=4)")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()