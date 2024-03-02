# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
numeros_pares = []
numeros_impares = []

while len(numeros) < 20:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    numeros_pares.append(numero) if numero % 2 == 0 else numeros_impares.append(numero)

print(numeros)
print(numeros_pares)
print(numeros_impares)