import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()
print("All Student Records (using fetchall):")
for row in rows:
    print(row)

cursor.close()
conn.close()
