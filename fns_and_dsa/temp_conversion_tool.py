#Defining Global Conversion Factors
fahrenheit_to_celcius_factor = (5/9)
celcius_to_fahrenheit_factor = (9/5)

#Temperature Conversion Fuctions
def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celcius_factor

def convert_to_fahrenheit(celcius):
    return (celcius * celcius_to_fahrenheit_factor) + 32

#User inputs for conversion
temp_input = input("Enter the temperature to convert: ")
try:
    temp = float(temp_input)  # Convert to float and check validity
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

#Perform Conversion
if unit == "F":
    result = convert_to_celcius(temp)
    print(f"{temp}°F is {result:.2f}°C")
elif unit == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result:.2f}°F")
else:
    raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


