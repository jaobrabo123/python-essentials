medias = []


for i in range(2):
    notas = []

    for a in range(4):
        nota = float(input(f"Digite a nota {a + 1} do aluno {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / 4
    medias.append(media)

alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7: {alunos_aprovados}")