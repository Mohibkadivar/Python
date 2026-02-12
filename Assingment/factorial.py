n = int(input("Enter the number you want to find factorial "))

fact =1
for i in range(2,n+1):
    fact = fact * i
print(fact)