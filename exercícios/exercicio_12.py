# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 16 anos possuem altura inferior à média de altura desses alunos.

num_alunos = 30
idades = []
alturas = []  

for n in range(num_alunos):
    idade = int(input(f'Digite a idade do aluno {n + 1}: '))
    idades.append(idade)
    altura = float(input(f'Digite a altura do aluno {n + 1}: '))
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)

contador = 0
for n in range(num_alunos):
    if idades[n] > 16 and alturas[n] < media_altura:
        contador += 1 

print(f"Quantidade de alunos com mais de 16 anos e altura inferior à média: {contador}")