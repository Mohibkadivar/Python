import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()

table_name = input("Enter table name to create: ")
n = int(input("Enter number of columns: "))

columns = []
for i in range(n):
    col_name = input(f"Enter column {i+1} name: ")
    col_type = input(f"Enter data type (varchar/int): ")
    col_size = input(f"Enter size: ")
    columns.append([col_name, col_type, col_size])

col_definitions = []
for col in columns:
    if col[1].lower() == 'varchar':
        col_definitions.append(f"{col[0]} VARCHAR({col[2]})")
    elif col[1].lower() == 'int':
        col_definitions.append(f"{col[0]} INT({col[2]})")

query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(col_definitions)})"
print("Executing:", query)
cursor.execute(query)
conn.commit()
print(f"Table '{table_name}' created successfully.")

cursor.close()
conn.close()
