import matplotlib.pyplot as plt

n = int(input("Enter number of courses: "))
courses = []
counts = []

for i in range(n):
    course = input(f"Enter Course {i+1} Name: ")
    count = int(input(f"Enter Number of Students in {course}: "))
    courses.append(course)
    counts.append(count)

max_index = counts.index(max(counts))
explode = [0.1 if i == max_index else 0 for i in range(n)]

plt.pie(counts, labels=courses, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title("Students per Course")
plt.tight_layout()
plt.savefig("course_pie_graph.png")
plt.show()
print("Pie graph saved as course_pie_graph.png")
