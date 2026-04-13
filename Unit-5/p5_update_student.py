import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

rollno = input("Enter Roll No to update: ")
cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
row = cursor.fetchone()

if row:
    name = input("Enter new Name: ")
    gender = input("Enter new Gender: ")
    age = int(input("Enter new Age: "))
    email = input("Enter new Email: ")
    mobile = input("Enter new Mobile: ")
    city = input("Enter new City: ")
    cursor.execute(
        "UPDATE student SET name=%s, gender=%s, age=%s, email=%s, mobile=%s, city=%s WHERE rollno=%s",
        (name, gender, age, email, mobile, city, rollno)
    )
    conn.commit()
    print("Student record updated successfully.")
else:
    print("Student not found.")

cursor.close()
conn.close()
