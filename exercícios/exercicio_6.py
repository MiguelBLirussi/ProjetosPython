# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
alunos_aprovados = 0

for i in range(1,11):
    print(f'Digite as 4 notas do aluno{i}')
    notas = [float(input(f"Nota {j}: ")) for j in range(1, 5)]
    media = sum(notas) / len(notas)
    alunos_aprovados = sum(1 for media in medias if media >= 7.0)
    medias.append(media)

print(f'- O número de alunos aprovados é: {alunos_aprovados} \n- As médias foram: {medias}')
    
    


