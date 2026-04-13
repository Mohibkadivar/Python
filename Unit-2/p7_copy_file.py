src = input("Enter source filename: ")
dst = input("Enter destination filename: ")

try:
    with open(src, 'r') as sf:
        content = sf.read()
    with open(dst, 'w') as df:
        df.write(content)
    print(f"File copied from '{src}' to '{dst}' successfully.")
except FileNotFoundError:
    print(f"Source file '{src}' not found.")
