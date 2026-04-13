import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("students.xlsx")

gender_counts = df['Gender'].value_counts()

plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink'])
plt.title("Male vs Female Students")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("gender_bar_graph.png")
plt.show()
print("Gender bar graph saved as gender_bar_graph.png")
