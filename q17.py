atleta = []
distancias = []
distancia = []
meds = []
i=0

while True:

    i = i+1
    nome = input(f'\nDigite o nome do {i}o atleta (não digite nada e dê enter para encerrar): ')
    if nome == '':
        break
    else:
        atleta.append(nome)
        distancia.clear()
        distancia1 = float(input('Digite a distância do 1o salto em metros: '))
        distancia.append(distancia1)
        distancia2 = float(input('Digite a distância do 2o salto em metros: '))
        distancia.append(distancia2)
        distancia3 = float(input('Digite a distância do 3o salto em metros: '))
        distancia.append(distancia3)
        distancia4 = float(input('Digite a distância do 4o salto em metros: '))
        distancia.append(distancia4)
        distancia5 = float(input('Digite a distância do 5o salto em metros: '))
        distancia.append(distancia5)
        meds.append((distancia1+distancia2+distancia3+distancia4+distancia5)/5)

        distancias.append(distancia)

print(f'\nAtletas e seus saltos:')

for u in range(0, len(atleta)):
    print(f'\nAtleta: {atleta[u]}')
    print(f'\nPrimeiro salto: {distancias[u][0]}')
    print(f'Segundo salto: {distancias[u][1]}')
    print(f'Terceiro salto: {distancias[u][2]}')
    print(f'Quarto salto: {distancias[u][3]}')
    print(f'Quinto salto: {distancias[u][4]}')

    print(f'\nRESULTADO:')
    print(f'\nAtleta: {atleta[u]}')
    print(f'Saltos: {distancias[u]}')
    print(f'Média: {meds[u]}')