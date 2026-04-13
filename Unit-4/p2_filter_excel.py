import pandas as pd

df = pd.read_excel("students.xlsx")

print("Students from Rajkot City:")
print(df[df['City'] == 'Rajkot'])

print("\nMale Students:")
print(df[df['Gender'] == 'Male'])

print("\nMale Students from Rajkot City:")
print(df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')])

print("\nStudents with Age >= 20:")
print(df[df['Age'] >= 20])
