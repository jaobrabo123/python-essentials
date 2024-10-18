total_mouses = 0
defeitos = [0] * 4

print("Registro de Mouses - Digite 0 para encerrar.")

while True:
    mouse_id = int(input("Número de identificação do mouse: "))
    if mouse_id == 0:
        break

    print("Tipos de defeito:")
    print("1- necessita da esfera")
    print("2- necessita de limpeza")
    print("3- necessita troca do cabo ou conector")
    print("4- quebrado ou inutilizado")

    defeito = int(input("Digite o número correspondente ao defeito: "))

    if 1 <= defeito <= 4:
        defeitos[defeito - 1] += 1
        total_mouses += 1
    else:
        print("Opção inválida. Escolha um defeito entre 1 e 4.")

print("\nRelatório:")
print(f"Quantidade de mouses: {total_mouses}")
print("Situação ---------------------- Quantidade  Percentual")
tipos_defeitos = [
    "1- necessita da esfera",
    "2- necessita de limpeza",
    "3- necessita troca do cabo ou conector",
    "4- quebrado ou inutilizado"
]

for i in range(4):
    percentual = (defeitos[i] / total_mouses) * 100 if total_mouses > 0 else 0
    print(f"{tipos_defeitos[i]:<30} {defeitos[i]:<10} {percentual:>5.1f}%")