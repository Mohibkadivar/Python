class Student:
    def __init__(self):
        self.rollno = None
        self.name = None
        self.age = None
        self.gender = None

    def AddStudent(self):
        self.rollno = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def DisplayStudent(self):
        print(f"\nRoll No : {self.rollno}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Gender  : {self.gender}")

s = Student()
s.AddStudent()
s.DisplayStudent()
