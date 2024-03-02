# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

while len(lista) < 10:
    numero = float(input('Digite um número: '))
    lista.append(numero)

print(sorted(lista,reverse=True))

