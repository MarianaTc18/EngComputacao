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

#loop que recebe as informações e adiciona data e hora
cont = 0
while (cont < 5):
       with open("dados.txt","r") as dados, open("dadoscomp.txt","a") as dadosc:
            limit = nLinhas("dados.txt")
            for i in range(0,limit):
                lertxt = dados.readline() #ler os dados no formato b'0,5.2\r\n'
                valor = str(lertxt.replace("b'","").replace("\\r\\n'", "")) #retira excessos
                valor2 = valor.strip()
                now = datetime.now() #captura data e hora
                data = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
                hora = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                #adicionada informações a dados completos no formato 0,5.2,13/11/2019,08:43:48
                escreve = dadosc.write(valor2 + "," + data + "," + hora + "\n")
                time.sleep(1)
                cont=cont + 1

#transforma o arquivo em csv
os.rename("dadoscomp.txt","dadoscomp.csv")

#passa os dados coletados para a planilha csv
with open("dadoscomp.csv","r") as dados:
        lercsv = pd.read_csv(dados, delimiter=',', quotechar = "\t", names=["Identificador","Valor Capturado", "Data", "Hora"])
        print(lercsv)
        lercsv.to_csv(r"planilha.csv", index = False, sep=',', quotechar = "\t")