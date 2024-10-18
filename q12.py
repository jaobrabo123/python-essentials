# Inicializa as listas para armazenar as idades e as alturas
idades = []
alturas = []


for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)


md_altura = sum(alturas) / len(alturas)


t_ac13 = sum(1 for idade in idades if idade > 13)


cont_inf_md = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < md_altura)


print(f"\nQuantidade de alunos com mais de 13 anos: {t_ac13}")
print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {cont_inf_md}")