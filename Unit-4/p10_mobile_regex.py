import pandas as pd
import re

df = pd.read_excel("students.xlsx")

mobile_pattern = re.compile(r'^\d{2}-\d{10}$')

valid = df[df['Mobile'].apply(lambda x: bool(mobile_pattern.match(str(x))))]

print("Records with Mobile Numbers having Country Code (e.g., 91-9999933333):")
print(valid)
