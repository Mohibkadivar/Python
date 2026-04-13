import zipfile
import os

def zip_files():
    zip_name = input("Enter zip file name (with .zip): ")
    files = input("Enter filenames to zip (comma separated): ").split(',')
    with zipfile.ZipFile(zip_name, 'w') as zf:
        for file in files:
            file = file.strip()
            if os.path.exists(file):
                zf.write(file)
                print(f"Added: {file}")
            else:
                print(f"File not found: {file}")
    print(f"Zip file '{zip_name}' created.")

def unzip_files():
    zip_name = input("Enter zip file name to extract: ")
    dest = input("Enter destination folder: ")
    with zipfile.ZipFile(zip_name, 'r') as zf:
        zf.extractall(dest)
    print(f"Files extracted to '{dest}'.")

print("1. Zip Files\n2. Unzip Files")
choice = input("Enter choice: ")
if choice == '1':
    zip_files()
elif choice == '2':
    unzip_files()
else:
    print("Invalid choice.")
