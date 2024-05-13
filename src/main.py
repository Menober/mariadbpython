import mariadb
import sys

try:
    # connection parameters
    conn_params = {
        'user': "root",
        'password': "mypass",
        'host': "127.0.0.1",
        'port': 3306
    }

    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

username = 'kokognieszka'

cursor.execute("USE database_python;")
cursor.execute("SELECT password FROM users WHERE username = '{}';".format(username))

result = cursor.fetchall()
for row in result:
    print(row)

connection.close()
cursor.close()

# print(cursor.execute("CREATE DATABASE database_python;"))
# cursor.execute("USE database_python;")
# print(cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50),password VARCHAR(50),name VARCHAR(50),surname VARCHAR(50));"))
# cursor.execute("INSERT INTO users (username, password, name, surname) VALUES ('kokognddieszka', 'I<3Arkadio', 'Aga', 'Kokoszka');")
# cursor.execute("COMMIT;")
# cursor.execute("SELECT * FROM users;")
