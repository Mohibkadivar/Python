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

email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

print("Records with Valid Email Addresses:")
for row in rows:
    if email_pattern.match(str(row[4])):
        print(row)

cursor.close()
conn.close()
