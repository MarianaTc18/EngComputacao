import csv
import pymysql
import pandas as pd

conexão = pymysql.connect(
    host='localhost',
    user='root',
    password='root1234',
    db ='importacao'
)
cursor = conexão.cursor()

cursor.execute("CREATE TABLE importcsv(hora VARCHAR(25), \
                Nome_Completo VARCHAR(255) , \
                Usuário_Afetado VARCHAR(255), \
                Contexto_Evento VARCHAR(255), \
                Componente VARCHAR(255), \
                Nome_evento VARCHAR(255)")

conexão.commit()

cursor.close()