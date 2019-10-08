import csv
import pymysql
import pandas as pd
import sys


def csv_to_mysql(load_sql, host, user, password):
    '''
    Esta função transfere informações de uma tabela no formato CSV para SQL de acordo com a variável load_sql
    '''
    try:
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='root1234',
                              autocommit=True,
                              local_infile=1)
        print('Conectando ao Banco de Dados: {}'.format(host))
        cursor = con.cursor()
        cursor.execute(load_sql)
        print('Sucesso na transferência da tabela.')
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


# Execution Example
load_sql = "LOAD DATA LOCAL INFILE '/home/mari/Documentos/import3.csv' INTO TABLE importacao.importcsv CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' ignore 1 lines;"
host = 'localhost'
user = 'root'
password = 'root1234'
csv_to_mysql(load_sql, host, user, password)