votos = []

while True:
    print('\n"Qual o melhor Sistema Operacional para uso em servidores?"\n')
    print('As possíveis respostas são:\n')
    print('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro')
    voto = int(input('\nDigite o seu voto (0 para sair): '))
    if (voto >= 1) and (voto <= 6):
        votos.append(voto)
    elif voto == 0:
        break
    else:
        while True:
            voto = int(input('Digite um voto valido (1 à 6 ou 0 para sair): '))
            if voto == 0:
                break
        if voto == 0:
            break
        else:
            votos.append(voto)

tot = len(votos)
votos1 = votos.count(1)
votos2 = votos.count(2)
votos3 = votos.count(3)
votos4 = votos.count(4)
votos5 = votos.count(5)
votos6 = votos.count(6)


print('\nSistema Operacional   Votos    %')
print('-------------------   -----   ---')
print(f'Windows Server        {votos1}         {(votos1/tot)*100}%')
print(f'Unix                  {votos2}         {(votos2/tot)*100}%')
print(f'Linux                 {votos3}         {(votos3/tot)*100}%')
print(f'Netware               {votos4}         {(votos4/tot)*100}%')
print(f'Mac OS                {votos5}         {(votos5/tot)*100}%')
print(f'Outro                 {votos6}         {(votos6/tot)*100}%')
