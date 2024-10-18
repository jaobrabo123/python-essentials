vetor = [0.0] * 10

for i in range(10):
    vetor[i] = float(input(f"Digite o {i+1}º número real: "))


print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])