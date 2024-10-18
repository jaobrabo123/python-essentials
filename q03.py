notas = [0] * 4

for i in range(0,4):
    notas[i] = float(input(f'Digite a sua {i+1}a nota: '))
    if i == 3:
        media = (notas[0]+notas[1]+notas[2]+notas[3])/4

print(f'\nSua média é: {media:.1f}')