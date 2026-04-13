filename = input("Enter filename: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
    print("File Contents:")
    print(content)
    words = content.split()
    print(f"\nTotal number of words: {len(words)}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
