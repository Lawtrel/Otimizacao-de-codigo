from scipy.optimize import curve_fit
import numpy as np

# Dados de tempo de execução para diferentes N
N = np.array([1000000, 10000000, 100000000, 1000000000])
tempo = np.array([0.5833094120025635, 0.5833094120025635, 5.964107990264893, 60.08355689048767])

# Definindo a função de custo
def custo(N, a, b, c):
    return a * N**2 + b * N + c

# Ajustando a curva aos dados
parametros, _ = curve_fit(custo, N, tempo)

# Extraindo os parâmetros
a, b, c = parametros

# Calculando o ponto crítico
N_critico = -b / (2 * a)

# Calculando o valor da função de custo no ponto crítico
custo_critico = custo(N_critico, a, b, c)

print("Parâmetros da função de custo:")
print("a =", a)
print("b =", b)
print("c =", c)
print("Ponto Crítico (N):", N_critico)
print("Custo no Ponto Crítico:", custo_critico)