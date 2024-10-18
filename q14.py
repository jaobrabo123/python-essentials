respostas = []

perguntas = [
    "Telefonou para a vítima? (s/n):",
    "Esteve no local do crime? (s/n):",
    "Mora perto da vítima? (s/n):",
    "Devia para a vítima? (s/n):",
    "Já trabalhou com a vítima? (s/n):"
]


for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    while resposta not in ['s', 'n']:
        print("Resposta inválida! Por favor, responda com 's' ou 'n'.")
        resposta = input(pergunta).strip().lower()
    respostas.append(resposta)


numero_de_sim = respostas.count('s')


if numero_de_sim == 2:
    classificacao = "Suspeita"
elif 3 <= numero_de_sim <= 4:
    classificacao = "Cúmplice"
elif numero_de_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"


print(f"\nClassificação: {classificacao}")