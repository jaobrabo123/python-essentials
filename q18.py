def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100 if total_votos > 0 else 0

votos = [0] * 23
total_votos = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    try:
        numero_jogador = int(input("Número do jogador (0=fim): "))

        if numero_jogador == 0:
            break
        elif 1 <= numero_jogador <= 23:
            votos[numero_jogador - 1] += 1
            total_votos += 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
    except ValueError:
        print("Por favor, insira um número válido.")

if total_votos == 0:
    print("Nenhum voto foi computado.")
else:
    print("\nResultado da votação:")
    print(f"Foram computados {total_votos} votos.")
    print("Jogador   Votos   %")

    jogadores_votados = [(i + 1, votos[i], calcular_percentual(votos[i], total_votos)) for i in range(23) if votos[i] > 0]

    for jogador, voto, percentual in jogadores_votados:
        print(f"{jogador:<9}{voto:<8}{percentual:>5.1f}%")

    # Encontrar o jogador com mais votos manualmente
    melhor_jogador = jogadores_votados[0][0]
    max_votos = jogadores_votados[0][1]
    percentual_melhor = jogadores_votados[0][2]

    for jogador, voto, percentual in jogadores_votados:
        if voto > max_votos:
            melhor_jogador = jogador
            max_votos = voto
            percentual_melhor = percentual

    print(f"\nO melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.")