import mymodule
from mymodule import add, subtract
from mymodule import multiply as mul

a = 10
b = 5

print("Using import mymodule:")
print("Add:", mymodule.add(a, b))
print("Divide:", mymodule.divide(a, b))

print("\nUsing from mymodule import:")
print("Subtract:", subtract(a, b))
print("Add:", add(a, b))

print("\nUsing alias:")
print("Multiply:", mul(a, b))
