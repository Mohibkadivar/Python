import mysql.connector
import re

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

pattern = re.compile(r'^N.{4}$')

print("Records where Name starts with 'N' and has length 5:")
for row in rows:
    if pattern.match(str(row[1])):
        print(row)

cursor.close()
conn.close()
