import csv
import pandas as pd
import sys
import os

os.rename("dados1.txt","dados1.csv")

with open("dados1.csv","r") as dados:
        ler = pd.read_csv(dados, delimiter=',', quotechar = "\t", names=["Identificador","Valor Capturado", "Data", "Hora"])
        print(ler)
        ler.to_csv(r"planilha.csv", index = False, sep=',', quotechar = "\t")