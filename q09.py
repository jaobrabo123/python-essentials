A = []
A2 = []

for i in range(0,10):
    num = int(input(f'Digite o {i+1}o número: '))
    A.append(num)
    A2.append(num**2)

print(f'\nSoma dos quadrados dos números digitados: {sum(A2)}')