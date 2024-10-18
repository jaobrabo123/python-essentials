modelos = []
consumos = []

for i in range(5):
    print(f"Veículo {i + 1}")
    modelo = input("Modelo: ").strip().lower()
    consumo = float(input("Km por litro: "))
    modelos.append(modelo)
    consumos.append(consumo)

preco_gasolina = 2.25
distancia = 1000

menor_consumo = float('inf')
carro_economico = ""

print("\nRelatório Final")
for i in range(5):
    litros = distancia / consumos[i]
    custo = litros * preco_gasolina
    print(f"{i + 1} - {modelos[i]} - {consumos[i]:.1f} - {litros:.1f} litros - R$ {custo:.2f}")

    if consumos[i] > menor_consumo:
        menor_consumo = consumos[i]
        carro_economico = modelos[i]

print(f"O menor consumo é do {carro_economico}.")