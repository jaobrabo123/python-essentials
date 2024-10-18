lista1 = []
lista2 = []
lista3 = []

for i in range(0,10):
    num = int(input(f'Digite o {i+1}o número da lista 1: '))
    lista1.append(num)

print('\n')

for i in range(0,10):
    num = int(input(f'Digite o {i+1}o número da lista 2: '))
    lista2.append(num)

print('\n')

for i in range(0,10):
    num = int(input(f'Digite o {i+1}o número da lista 3: '))
    lista3.append(num)

lista4 = lista1
lista4.extend(lista2)
lista4.extend(lista3)

print(f'\nNúmeros de todas as listas: {lista4}')