filename = input("Enter filename with numbers: ")

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
    numbers = [float(line.strip()) for line in lines if line.strip()]
    print("Numbers:", numbers)
    print("Total:", sum(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except ValueError:
    print("File contains non-numeric data.")
