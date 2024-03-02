# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = []
for n in range(1,11):
    numero = int(input(f'Digite o {n}º: '))
    numero_quadrado = numero * numero
    numeros.append(numero_quadrado)

soma = sum(numeros)
print(f'- Números ao quadrado: {numeros}\n- Soma do quadrado dos números: {soma}')