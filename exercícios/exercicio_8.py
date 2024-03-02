# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = []
idades = []
alturas = []

for pessoa in range(1,6):
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    altura = float(input(f'Digite a altura da {pessoa}ª pessoa: '))
    idades.append(idade)
    alturas.append(altura)
    pessoas.append(pessoa)

print(f' Pessoas:{sorted(pessoas,reverse=True)}')
print(f' Alturas:{sorted(alturas,reverse=True)}')
print(f' Idades:{sorted(idades,reverse=True)}')

