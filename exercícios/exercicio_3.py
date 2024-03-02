# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []

while len(lista) < 4:
    numero = float(input('- Digite um número: '))
    lista.append(numero)

nota1 = lista[0]
nota2 = lista[1]
nota3 = lista[2]
nota4 = lista[3]
divisor = len(lista)
soma_notas = nota1 + nota2 + nota3 + nota4
media = (soma_notas / divisor)
print(f'- Média das notas: {media}')