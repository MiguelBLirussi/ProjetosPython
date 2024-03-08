from datetime import date
from datetime import timedelta
import os

d = input('Digite a data que deseja calcular, no formato DD/MM/AAAA:')
dia = int(d[0:2])
mes = int(d[3:5])
ano = int(d[6:])
data = date(ano,mes,dia)

dias_40_55 = []
dias_56_109 = []
dias_110_115 = []

os.system('cls')

print('\nDatas de 40 a 55 dias pra frente\n')
dias = 40
while len(dias_40_55) != 16:
    dias_soma = timedelta(days=dias)
    data_calculada = data + dias_soma
    dias_40_55.append(data_calculada)
    dias += 1
    print(data_calculada)

print('\nDatas de 56 a 109 dias pra frente\n')
while len(dias_56_109) != 54:
    dias_soma = timedelta(days=dias)
    data_calculada = data + dias_soma
    dias_56_109.append(data_calculada)
    dias += 1
    print(data_calculada)

print('\nDatas de 110 a 115 dias pra frente\n')
while len(dias_110_115) != 6:
    dias_soma = timedelta(days=dias)
    data_calculada = data + dias_soma
    dias_110_115.append(data_calculada)
    dias += 1
    print(data_calculada)


dias_40_55.clear()
dias_56_109.clear()
dias_110_115.clear()


print('\nDatas de 40 a 55 dias pra trás\n')
dias = 40
while len(dias_40_55) != 16:
    dias_soma = timedelta(days=dias)
    data_calculada = data - dias_soma
    dias_40_55.append(data_calculada)
    dias += 1
    print(data_calculada)

print('\nDatas de 56 a 109 dias pra trás\n')
while len(dias_56_109) != 54:
    dias_soma = timedelta(days=dias)
    data_calculada = data - dias_soma
    dias_56_109.append(data_calculada)
    dias += 1
    print(data_calculada)

print('\nDatas de 110 a 115 dias pra trás\n')
while len(dias_110_115) != 6:
    dias_soma = timedelta(days=dias)
    data_calculada = data - dias_soma
    dias_110_115.append(data_calculada)
    dias += 1
    print(data_calculada)
    

