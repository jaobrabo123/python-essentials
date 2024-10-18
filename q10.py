vetor1 = []
vetor2 = []

print("lista 1: Digite 10 numeros")
for i in range(10):
    elemento = int(input(f"Número L1: {i+1}: "))
    vetor1.append(elemento)


print(" lista 2: Digite 10 números")
for i in range(10):
    elemento = int(input(f"Número L2: {i+1}: "))
    vetor2.append(elemento)

vetor3 = []

for i in range(10):
    vetor3.extend([vetor1[i], vetor2[i]])

print("\nVetor intercalado:")
print(vetor3)