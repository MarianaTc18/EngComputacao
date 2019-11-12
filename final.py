import csv
import pandas as pd
import sys
import os

#os.rename("dados1.txt","dados1.csv")

with open("dados1.csv","r") as dados:
        ler = pd.read_csv(dados, delimiter=',', quotechar = "\t")
        print(ler)
        ler.to_csv(r"planilha1.csv", header=["Identificador","Valor Capturado", "Data", "Hora"], index = False, sep=',', quotechar = "\t")

with open("planilha1.csv","r") as planilha:
        lerp = pd.read_csv(planilha, delimiter=',', quotechar = "\t")
        print("\n", lerp)