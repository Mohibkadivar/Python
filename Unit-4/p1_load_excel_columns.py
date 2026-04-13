import pandas as pd

df = pd.read_excel("students.xlsx")
print("Columns and Data Types:")
print(df.dtypes)
print("\nShape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())
