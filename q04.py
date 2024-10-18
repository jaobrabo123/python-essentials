vogais = 'aeiouAEIOU'
alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

vetor = [input(f"Digite o {i+1}º caractere: ") for i in range(10)]


consoantes = [char for char in vetor if char in alfabeto and char not in vogais]


print(f"Consoantes lidas: {len(consoantes)}")
print("Consoantes:", ' '.join(consoantes))