import matplotlib.pyplot as plt

ages = []
print("Enter age of 50 students:")
for i in range(50):
    age = int(input(f"Student {i+1} Age: "))
    ages.append(age)

bins = [0, 10, 20, 30, 40, 50, 60, 120]
plt.hist(ages, bins=bins, edgecolor='black', color='orange')
plt.title("Age Distribution of Students")
plt.xlabel("Age Group")
plt.ylabel("Number of Students")
plt.xticks(bins)
plt.tight_layout()
plt.savefig("age_histogram.png")
plt.show()
print("Histogram saved as age_histogram.png")
