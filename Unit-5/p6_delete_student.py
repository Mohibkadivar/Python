import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

rollno = input("Enter Roll No to delete: ")
cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
row = cursor.fetchone()

if row:
    cursor.execute("DELETE FROM student WHERE rollno = %s", (rollno,))
    conn.commit()
    print("Student record deleted successfully.")
else:
    print("Student not found.")

cursor.close()
conn.close()
