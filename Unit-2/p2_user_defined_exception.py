class AgeInvalidError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def check_age(age):
    if age < 0 or age > 150:
        raise AgeInvalidError(f"Age {age} is not valid. Must be between 0 and 150.")
    return age

try:
    age = int(input("Enter age: "))
    check_age(age)
    print("Valid age:", age)
except AgeInvalidError as e:
    print("User Defined Exception caught:", e)
except ValueError:
    print("Please enter a numeric value.")
