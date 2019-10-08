import csv
import pymysql
import pandas as pd

conexão = pymysql.connect(
    host='localhost',
    user='root',
    password='root1234'
)
cursor = conexão.cursor()

cursor.execute("CREATE DATABASE importacao")

conexão.commit()

cursor.close()
