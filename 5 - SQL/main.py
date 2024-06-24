import os
import dotenv
import sqlite3
from pathlib import Path
import pymysql
import pymysql.cursors
from typing import cast

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
CURRENT_CURSOR = pymysql.cursors.SSDictCursor   # Changing the cursor to return a Dict instead an Array

dotenv.load_dotenv()

conn = sqlite3.connect(DB_FILE)         # do this for a SQL File (dq.sqlite3)
conn = pymysql.connect(                 # do this for a SQL Server Connection
    host=os.environ['VAR...'],          # dotenv file
    user=os.environ['VAR...'],
    password=os.environ['VAR...'],
    database=os.environ['VAR...'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR          
)
cursor = conn.cursor()


cursor.execute(f'CREATE TABLE IF NOT EXISTS customers (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(100))')
conn.commit()


sql = (f'INSERT INTO ...(valor1, valor2) VALUES (?, ?)')
cursor.execute(sql, ['Joana', 41])                              # Insere 1 só
cursor.executemany(sql, (('Joana', 41), ('Paulo', 21)))         # Insere vários
conn.commit()


sql = (f'UPDATE ... SET nome=%s, idade=%d WHERE id=%s')         # Usando %s %d...
cursor.mogrify(sql)                                             # Mostra a query sql sem executá-la
cursor.execute(sql, ('Eleonor', 34, 4))
conn.commit()


cursor.execute('SELECT * FROM ...')
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)


row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)


rows = cursor.fetchall()
print(cursor.rowcount)          # Conta o número de linhas
print(cursor.lastrowid)         # Último ID inserido na base de dados
print(cursor.rownumber)         # Número da linha


with conn.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)           # Convert cursor return type

        sql = (f'INSERT INTO ... (nome, idade) VALUES (%(name)s, %(age)s)')

        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)             # Inserindo um valor usando dicionários

        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Júlia", "age": 74, },
            {"name": "Rose", "age": 53, },
        )
        result = cursor.executemany(sql, data3)         # Inserindo vários valores usado dicionários


cursor.close()
conn.close()