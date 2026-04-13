import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

rollno = input("Enter Roll No to search: ")
cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
row = cursor.fetchone()

if row:
    print(f"Roll No : {row[0]}")
    print(f"Name    : {row[1]}")
    print(f"Gender  : {row[2]}")
    print(f"Age     : {row[3]}")
    print(f"Email   : {row[4]}")
    print(f"Mobile  : {row[5]}")
    print(f"City    : {row[6]}")
else:
    print("Student not found.")

cursor.close()
conn.close()
