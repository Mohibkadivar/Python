# 3. Function to Calculate Factorial (Using Recursion)
# ~ Implement factorial using:
# -> Normal function
# -> Recursive function


def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:    
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))