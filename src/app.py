from flask import Flask
import pymysql
from config import DB_CONFIG

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
        return f"Hola Mundo desde Flask! Conectado a MySQL {version[0]}"
    except Exception as e:
        return f"Error al conectar a MySQL: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
