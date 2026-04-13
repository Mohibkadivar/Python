import os

FILENAME = 'students.txt'

def add_student():
    rollno = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    with open(FILENAME, 'a') as f:
        f.write(f"{rollno},{name},{age}\n")
    print("Student added successfully.")

def search_student():
    rollno = input("Enter Roll No to search: ")
    found = False
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if parts[0] == rollno:
                    print(f"Roll No: {parts[0]}, Name: {parts[1]}, Age: {parts[2]}")
                    found = True
    except FileNotFoundError:
        pass
    if not found:
        print("Student not found.")

def list_students():
    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
        if not lines:
            print("No students found.")
        for line in lines:
            parts = line.strip().split(',')
            print(f"Roll No: {parts[0]}, Name: {parts[1]}, Age: {parts[2]}")
    except FileNotFoundError:
        print("No records found.")

def update_student():
    rollno = input("Enter Roll No to update: ")
    updated = False
    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
        with open(FILENAME, 'w') as f:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == rollno:
                    name = input("Enter new Name: ")
                    age = input("Enter new Age: ")
                    f.write(f"{rollno},{name},{age}\n")
                    updated = True
                else:
                    f.write(line)
    except FileNotFoundError:
        print("No records found.")
        return
    print("Updated successfully." if updated else "Student not found.")

def delete_student():
    rollno = input("Enter Roll No to delete: ")
    deleted = False
    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
        with open(FILENAME, 'w') as f:
            for line in lines:
                if line.strip().split(',')[0] != rollno:
                    f.write(line)
                else:
                    deleted = True
    except FileNotFoundError:
        print("No records found.")
        return
    print("Deleted successfully." if deleted else "Student not found.")

while True:
    print("\n1. Add Student\n2. Search Student\n3. List All Students\n4. Update Student\n5. Delete Student\n6. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        list_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
