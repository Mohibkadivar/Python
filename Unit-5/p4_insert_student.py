import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

rollno = input("Enter Roll No: ")
name = input("Enter Name: ")
gender = input("Enter Gender: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
mobile = input("Enter Mobile: ")
city = input("Enter City: ")

cursor.execute(
    "INSERT INTO student (rollno, name, gender, age, email, mobile, city) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (rollno, name, gender, age, email, mobile, city)
)
conn.commit()
print("Student record inserted successfully.")

cursor.close()
conn.close()
