import csv
import pymysql
import pandas as pd

conexão = pymysql.connect(
    host='localhost',
    user='root',
    password='root1234',
    db='teste1'
)
cursor = conexão.cursor()

cursor.execute('SELECT* FROM teste1;')

resultado = cursor.fetchall()

for linha in resultado :
    print(linha)

conexão.commit()

cursor.close()