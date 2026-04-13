import logging

logging.basicConfig(filename='arithmetic_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError: %s", e)
    print("Error logged: Cannot divide by zero.")
except ValueError as e:
    logging.error("ValueError: %s", e)
    print("Error logged: Invalid input.")
