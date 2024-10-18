nums = []
par = []
impar = []

for i in range(0,20):
    num = int(input(f'Digite o {i+1}o número: '))
    nums.append(num)
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Todos os números: {nums}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')