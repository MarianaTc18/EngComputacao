import csv
import pymysql
import pandas as pd

conexão = pymysql.connect(
    host='localhost',
    user='root',
    password='root1234',
    db='teste1')
cursor = conexão.cursor()

cursor.execute('INSERT INTO importcsv(hora, \
                    nome_completo, \
                    contexto_evento, \
                    componente, \
                    nome_evento) VALUES ("24/09/2019 23:58", "ELIANE DE SOUSA ARAUJO", "Fórum: Fórum de esclarecimento de dúvidas com o professor", "Fórum", "Algum conteúdo foi publicado.");');

conexão.commit()

cursor.close()
print("Concluído")



