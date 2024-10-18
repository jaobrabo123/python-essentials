mes = []
med = []
temps = []
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

for i in range(0,12):
    temp = float(input(f'Digite a temperatura média de {meses[i]}: '))
    mes.append(temp)

for i in range(0,12):
    if mes[i] > (sum(mes)/12):
        med.append(meses[i])
        temps.append(mes[i])

print('\nMeses que tiveram a temperatura acima da média anual:\n')

for i in range(0, len(med)):
    print(f'{med[i]}: {temps[i]}')