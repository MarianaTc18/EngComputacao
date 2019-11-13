import pandas as pd
import os
import time
from datetime import datetime

#função que calcula o número de linhas em um arquivo
def nLinhas (nomeArquivo):
    arquivo = open(nomeArquivo, "r");
    linhaUnica = "";
    for linha in arquivo:
        linhaUnica += linha + "#";
    arquivo.close();
    linhas = linhaUnica.split("#");
    nlinhas = len(linhas) - 1;
    return nlinhas;

#criaplanilha
#with open("planilha.csv", "w") as dados:
 #   escreve2 = dados.write("Identificador,Valor Capturado, Data, Hora\n")

#loop que recebe as informações e adiciona data e hora
cont = 0
while (cont < 1):
       with open("dados.txt","r") as dados, open("planilha.csv","w") as planilha:
            limit = nLinhas("dados.txt")
            escreve2 = planilha.write("Identificador,Valor Capturado, Data, Hora\n")
            for i in range(0,limit):
                lertxt = dados.readline() #ler os dados no formato b'0,5.2\r\n'
                valor = str(lertxt.replace("b'","").replace("\\r\\n'", "")) #retira excessos
                valor2 = valor.strip()
                now = datetime.now() #captura data e hora
                data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
                hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                #adicionada informações a dados completos no formato 0,5.2,13/11/2019,08:43:48
                formato = valor2 + "," + data + "," + hora + "\n"
                escreve = planilha.write(formato)
                time.sleep(1)
       with open("planilha.csv", "r") as planilha:
            lercsv = pd.read_csv(planilha)
            print(lercsv)
       cont = cont + 1