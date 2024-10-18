print("Projeção de Gastos com Abono (0 para sair!)\n============================")
salarios, total_abonos, min_abono_count, maior_abono = [], 0, 0, 0

while True:
    salario = float(input("Salário: "))
    if salario == 0: break
    abono = max(salario * 0.20, 100)
    salarios.append((salario, abono))
    total_abonos += abono
    if abono == 100: min_abono_count += 1
    if abono > maior_abono: maior_abono = abono

print("\nSalário - Abono")
for salario, abono in salarios:
    print(f"R$ {salario:.2f} - R$ {abono:.2f}")

print(f"\nForam processados {len(salarios)} colaboradores")
print(f"Total gasto com abonos: R$ {total_abonos:.2f}\n")
print(f"Valor mínimo pago a {min_abono_count} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")