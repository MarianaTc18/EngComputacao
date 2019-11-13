import pandas as pd
import os
import time
from datetime import datetime

#função que adiciona data e hora
def formatoCsv(valor):
    valor1 = str(valor.replace("b'", "").replace("\\r\\n'", ""))  # retira excessos
    valor2 = valor1.strip()
    now = datetime.now()  # captura data e hora
    data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    # adicionada informações a dados completos no formato 0,5.2,13/11/2019,08:43:48
    formato = valor2 + "," + data + "," + hora + "\n"
    return formato

#criaplanilha
with open("planilha.csv", "w") as dados:
    escreve2 = dados.write("Identificador,Valor Capturado, Data, Hora\n")

#loop que recebe as informações e adiciona data e hora
cont = 0
while (cont < 3):
       with open("dados5.txt","r") as dados, open("planilha.csv","a") as planilha:
                lines = dados.readlines() #ler os dados no formato b'0,5.2\r\n'
                planilha.write(formatoCsv(lines[cont]))
                time.sleep(1)
       with open("planilha.csv", "r") as planilha:
            lercsv = pd.read_csv(planilha)
            print(lercsv)
       with open("dados5.txt", "a") as dados: # comando provisório
           escreve = dados.write("\nb'0,47.3\\r\\n'")
       cont = cont + 1
