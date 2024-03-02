# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_a = []
vetor_b = []
vetor_c = []

for n in range(1,11):
    num = float(input(f'Digite o {n}º do vetor A: '))
    vetor_a.append(num)
    num = float(input(f'Digite o {n}º do vetor B: '))
    vetor_b.append(num)
    num = float(input(f'Digite o {n}º do vetor C: '))
    vetor_c.append(num)

def intercalar_vetores(vetor_a, vetor_b, vetor_c):
    vetor_abc = []
    for n_a,n_b,n_c in zip(vetor_a,vetor_b, vetor_c):
        vetor_abc.append(n_a)
        vetor_abc.append(n_b)
        vetor_abc.append(n_c)
    return vetor_abc

print(f'- Vetor A: {vetor_a}\n- Vetor B: {vetor_b}\n- Vetor C: {vetor_c}\n- Vetor Intercalado: {intercalar_vetores(vetor_a,vetor_b,vetor_c)}')