num = []

for i in range(0,5):
    n = int(input(f'Digite o {i+1}o número: '))
    num.append(n)

soma = sum(num)
mult = 1

for i in range(0,5):
    mult *= num[i]

print(f'\nNúmeros: {num}')
print(f'Soma: {soma}')
print(f'Multiplicação: {mult}')