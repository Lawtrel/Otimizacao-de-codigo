import matplotlib.pyplot as plt
import numpy as np

# Definindo a função de custo
def custo(N, a, b, c):
    return a * N**2 + b * N + c

# Parâmetros encontrados
a = 3.66e-18
b = 5.61e-08
c = 0.28

# Gerando valores de N para o gráfico
N = np.linspace(0, 1000000000000, 100)  # Valores de 0 a 10000 para o eixo X

# Calculando os valores de custo para os valores de N
custos = custo(N, a, b, c)

# Calculando o ponto crítico
N_critico = -b / (2 * a)
custo_critico = custo(N_critico, a, b, c)

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(N, custos, label='Custo (C(N))')
plt.scatter(N_critico, custo_critico, color='red', label='Ponto Crítico')
plt.title('Função de Custo e Ponto Crítico')
plt.xlabel('N')
plt.ylabel('Custo (segundos)')
plt.legend()
plt.grid(True)
plt.show()
