# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []

while len(numeros) < 5:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

soma = sum(numeros)
multiplicacao = 1
for num in numeros:
    multiplicacao *= num 

print(f'Números: {numeros}')
print(f'Soma dos números: {soma}')
print(f'Multiplicação dos números: {multiplicacao}')

