intervalos = [0] * 8

def calcular_salario(vendas_brutas):
    return 200 + (0.09 * vendas_brutas)


numero_vendedores = int(input("Digite o número de vendedores: "))


for i in range(numero_vendedores):
    vendas_brutas = float(input(f"Digite as vendas brutas do vendedor {i + 1}: "))
    salario = calcular_salario(vendas_brutas)


    if salario < 200:
        continue
    elif salario >= 1000:
        intervalo = 7
    else:
        intervalo = int((salario - 200) // 100)

    intervalos[intervalo] += 1

# Exibe os resultados
print("\nContagem de vendedores por intervalo de salário:")
print(f"$200 - $299: {intervalos[0]}")
print(f"$300 - $399: {intervalos[1]}")
print(f"$400 - $499: {intervalos[2]}")
print(f"$500 - $599: {intervalos[3]}")
print(f"$600 - $699: {intervalos[4]}")
print(f"$700 - $799: {intervalos[5]}")
print(f"$800 - $899: {intervalos[6]}")
print(f"$900 - $999: {intervalos[7]}")
print(f"$1000 e acima: {intervalos[7]}")