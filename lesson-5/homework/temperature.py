def convert_cel_to_far(celsius_value: float) -> float:
    return celsius_value * 9 / 5 + 32

def convert_far_to_cel(fahrenheit_value: float) -> float:
    return (fahrenheit_value - 32) * 5 / 9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit}°F is {celsius:.2f}°C")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = convert_cel_to_far(celsius)
print(f"{celsius}°C is {fahrenheit:.2f}°F")