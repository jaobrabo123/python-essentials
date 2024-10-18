import random

contadores = [0] * 6


for _ in range(100):
    contadores[random.randint(1, 6) - 1] += 1


print("Resultados dos lançamentos de dados:")
for i in range(6):
    print(f"Valor {i + 1}: {contadores[i]} vezes")