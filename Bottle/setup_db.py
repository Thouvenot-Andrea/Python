import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="Andrea",
    password="HelioS@@du26",
    database="Bottle"
)
c = conn.cursor()

# Créer une table exemple
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
)
''')

conn.commit()
conn.close()

