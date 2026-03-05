# Menu Driven Program: Student Result

marks = []

def enter_marks():
    global marks
    n = int(input("Enter number of subjects: "))
    marks = []
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    print("Marks entered successfully!")

def calculate_percentage():
    if not marks:
        print("No marks entered!")
        return
    total = sum(marks)
    per = (total / len(marks))
    print(f"Percentage: {per:.2f}%")

def assign_grade():
    if not marks:
        print("No marks entered!")
        return
    total = sum(marks)
    per = (total / len(marks))
    
    if per >= 90:
        grade = "A"
    elif per >= 80:
        grade = "B"
    elif per >= 70:
        grade = "C"
    elif per >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Grade: {grade}")

while True:
    print("\n1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")
    ch = input("Enter choice: ")
    
    if ch == '1':
        enter_marks()
    elif ch == '2':
        calculate_percentage()
    elif ch == '3':
        assign_grade()
    elif ch == '4':
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
