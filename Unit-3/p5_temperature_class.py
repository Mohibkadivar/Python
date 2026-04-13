class Temperature:
    def __init__(self, value):
        self.value = value

    def convertFarenheit(self):
        return (self.value * 9/5) + 32

    def convertCelsius(self):
        return (self.value - 32) * 5/9

print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
choice = input("Enter choice: ")
val = float(input("Enter temperature value: "))
t = Temperature(val)

if choice == '1':
    print(f"{val}°C = {t.convertFarenheit():.2f}°F")
elif choice == '2':
    print(f"{val}°F = {t.convertCelsius():.2f}°C")
