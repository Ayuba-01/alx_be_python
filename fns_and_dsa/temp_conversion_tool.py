FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


answer = int(input("Enter the temperature to convert: "))
answer2 = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

if answer2 == "F":
    print(f"{answer}.0F is {convert_to_celsius(answer)}")

elif answer2 == "C":
    print(f"{answer}.0C is {convert_to_fahrenheit(answer)}")
    
else:
    print("Invalid temperature. Please enter a numeric value.")