import time

def soma_quadrados(N):
    soma = 0
    for i in range(1, N+1):
        soma += i**2
    return soma

# Medir o tempo de execução
start_time = time.time()
resultado = soma_quadrados(1000000000)  # Calcular a soma dos quadrados até 1 milhão
end_time = time.time()

tempo_execucao = end_time - start_time
print("Resultado:", resultado)
print("Tempo de Execução:", tempo_execucao, "segundos")