import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )

def insert_student():
    conn = get_connection()
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
    print("Student inserted successfully.")
    cursor.close()
    conn.close()

def update_student():
    conn = get_connection()
    cursor = conn.cursor()
    rollno = input("Enter Roll No to update: ")
    cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
    if cursor.fetchone():
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
        print("Student updated successfully.")
    else:
        print("Student not found.")
    cursor.close()
    conn.close()

def search_student():
    conn = get_connection()
    cursor = conn.cursor()
    rollno = input("Enter Roll No to search: ")
    cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
    row = cursor.fetchone()
    if row:
        print(f"Roll No: {row[0]}, Name: {row[1]}, Gender: {row[2]}, Age: {row[3]}, Email: {row[4]}, Mobile: {row[5]}, City: {row[6]}")
    else:
        print("Student not found.")
    cursor.close()
    conn.close()

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    rollno = input("Enter Roll No to delete: ")
    cursor.execute("SELECT * FROM student WHERE rollno = %s", (rollno,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM student WHERE rollno = %s", (rollno,))
        conn.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")
    cursor.close()
    conn.close()

def list_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    if rows:
        print(f"{'RollNo':<10} {'Name':<20} {'Gender':<8} {'Age':<5} {'Email':<25} {'Mobile':<15} {'City':<15}")
        print("-" * 100)
        for row in rows:
            print(f"{row[0]:<10} {row[1]:<20} {row[2]:<8} {row[3]:<5} {row[4]:<25} {row[5]:<15} {row[6]:<15}")
    else:
        print("No records found.")
    cursor.close()
    conn.close()

while True:
    print("\n1. Insert Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. List Students")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        insert_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        list_students()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
