filename = input("Enter marks file name (CSV): ")

try:
    with open(filename, 'r') as f:
        lines = f.readlines()

    print(f"{'RollNo':<10} {'Name':<20} {'M1':>5} {'M2':>5} {'M3':>5} {'M4':>5} {'Total':>7} {'%':>7} {'Grade':>6}")
    print("-" * 70)

    for line in lines:
        parts = line.strip().split(',')
        if len(parts) < 6:
            continue
        rollno = parts[0]
        name = parts[1]
        marks = list(map(float, parts[2:6]))
        total = sum(marks)
        percentage = total / 4
        if percentage >= 70:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 40:
            grade = 'D'
        else:
            grade = 'F'
        print(f"{rollno:<10} {name:<20} {marks[0]:>5} {marks[1]:>5} {marks[2]:>5} {marks[3]:>5} {total:>7} {percentage:>7.2f} {grade:>6}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
