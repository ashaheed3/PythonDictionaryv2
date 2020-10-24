import mysql.connector
from decouple import config

USER = config('database_user')
PASSWORD = config('database_password')
HOST = config('database_host')
DATABASE = config('database_name')


con = mysql.connector.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    database=DATABASE
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM DICTIONARY")
results = cursor.fetchall()

print(results)