# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

while len(lista) < 5:
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(lista)