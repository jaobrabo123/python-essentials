notas = []
nota=0
i=0

while nota != -1:
    i = i + 1
    nota = float(input(f'Digite a sua {i}a nota (-1 para encerrar): '))
    if nota == -1:
        break
    else:
        notas.append(nota)

print(f'\nVocê digitou {len(notas)} notas.')
print(f'Notas que você digitou: {notas}')
print(f'Notas na ordem inversa em que foram digitadas:')
for i in range(len(notas), 0, -1):
    print(notas[(i-1)])
print(f'Soma das notas: {sum(notas)}')
print(f'Média das notas: {sum(notas)/len(notas)}')
acdamedia = []
abde7 = []
for i in range(0, len(notas)):
    if notas[i] > sum(notas)/len(notas):
        acdamedia.append(notas[i])
    if notas[i] < 7:
        abde7.append(notas[i])
print(f'Quantidade de notas acima da média das notas: {len(acdamedia)}')
print(f'Quantidade de notas abaixo de 7: {len(abde7)}')
print('\nFIM!')
