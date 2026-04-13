class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print(f"Roll No: {self.rollno}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}")

class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        self.display_student()
        print(f"Course: {self.coursename}, Duration: {self.duration}, Fee: {self.fee}")

c = Course("101", "Rahul", "Male", 21, "MCA", "2 Years", 50000)
c.display_course()
