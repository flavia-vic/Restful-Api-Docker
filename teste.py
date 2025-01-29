import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='flask-api-restful',
        port=3306  # Porta padrão do MariaDB
    )
    print("Conexão ao MariaDB bem-sucedida!")
except pymysql.MySQLError as e:
    print(f"Erro ao conectar ao MariaDB: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
