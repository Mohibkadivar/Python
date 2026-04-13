import pandas as pd
import re

df = pd.read_excel("students.xlsx")

email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

valid = df[df['E-Mail'].apply(lambda x: bool(email_pattern.match(str(x))))]

print("Records with Valid Email Addresses:")
print(valid)
