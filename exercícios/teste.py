from datetime import date
from datetime import timedelta


data = date(2024,3,7)
dias = 40
dias_soma = timedelta(days=dias)
data_calculada = data - dias_soma

print(data_calculada)