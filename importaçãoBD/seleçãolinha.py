import csv
import pandas as pd

csv_data = pd.read_csv('/home/mari/Documentos/import1.csv')


for row in csv_data:
      print(csv_data["componente"][row])
