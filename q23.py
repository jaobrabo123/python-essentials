usuarios = []
usos = []

def verificar_limite(name):
    while True:
        nome = name
        while len(nome) > 15:
            nome = input(f'O limite é de 15 caracteres, digite novamente: ')
        while len(nome) < 15:
            nome = nome+' '
        return nome
def bytes_para_mb(bytes):
    mb = bytes/1000000
    return mb
while True:
    name = input('\nDigite o seu nome (0 para encerrar): ')
    if name == '0':
        break
    nome = verificar_limite(name)
    bytes = int(input('Quantos bytes você está usando?: '))
    mb = bytes_para_mb(bytes)
    usuarios.append(nome)
    usos.append(mb)

print('\n-=-=-=-=-ARMAZENAMENTO USADO PELOS FUNCIONÁRIOS-=-=-=-=-')
print('Número | Nome            |      Espaço Usado     | % do uso')
total = sum(usos)

for i in range(0, len(usuarios)):
    print(f'{i+1}      | {usuarios[i]} |   {usos[i]:.2f}MB    | {((usos[i]/total) * 100):.2f}%')

print(f'\nEspaço total usado: {(total):.2f}MB')
print(f'Média de uso: {(total/len(usos)):.2f}MB')