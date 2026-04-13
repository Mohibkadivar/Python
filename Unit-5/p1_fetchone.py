import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")

print("All Student Records (using fetchone):")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

cursor.close()
conn.close()
