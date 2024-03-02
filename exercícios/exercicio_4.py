# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

palavra = ''
while len(palavra) < 10:
    palavra = input('Digite uma palavra de 10 letras: ')

consoantes = []
num_consoantes = 0
for i in palavra:
    if i not in 'AEIOUaeiou':
        num_consoantes += 1
        if i not in consoantes:
            consoantes.append(i)

print(f'A palavra: {palavra} tem {num_consoantes} consoantes , são elas {sorted(consoantes)}')
