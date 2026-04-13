import pandas as pd

df = pd.read_excel("students.xlsx")

print("Original Data:")
print(df)

print("\nAfter dropna() - Rows with any null removed:")
df_dropped = df.dropna()
print(df_dropped)

print("\nAfter fillna('N/A') - Nulls filled with 'N/A':")
df_filled = df.fillna("N/A")
print(df_filled)
