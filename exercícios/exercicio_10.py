#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = []
vetor_b = []

for n in range(1,11):
    num = float(input(f'Digite o {n}º do vetor A: '))
    vetor_a.append(num)
    num = float(input(f'Digite o {n}º do vetor B: '))
    vetor_b.append(num)

def intercalar_vetores(vetor_a, vetor_b):
    vetor_ab = []
    for n_a,n_b in zip(vetor_a,vetor_b):
        vetor_ab.append(n_a)
        vetor_ab.append(n_b)
    return vetor_ab

print(f'- Vetor A: {vetor_a}\n- Vetor B: {vetor_b}\n- Vetor Intercalado: {intercalar_vetores(vetor_a,vetor_b)}')
