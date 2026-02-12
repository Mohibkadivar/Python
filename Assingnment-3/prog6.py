
balance = 0.0

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount}")
        print(f"Updated Balance: ${balance}")
    else:
        print("Invalid deposit amount!")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Invalid withdrawal amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Withdrawn: ${amount}")
        print(f"Remaining Balance: ${balance}")

def check_balance():
    print(f"Current Balance: ${balance}")

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thank you for using the banking system!")
        break
    else:
        print("Invalid choice! Please try again.")
