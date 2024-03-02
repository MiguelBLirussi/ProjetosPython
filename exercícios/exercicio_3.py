# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

while len(notas) < 4:
    numero = float(input('- Digite uma nota: '))
    notas.append(numero)

media = (sum(notas) / len(notas))
print(f'- Média das notas: {media}')