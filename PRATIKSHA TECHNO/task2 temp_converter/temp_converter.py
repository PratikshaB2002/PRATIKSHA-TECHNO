def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def temperature_converter():
    print("Temperature Converter")

    # Get user input for temperature and unit
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ").upper()

    # Perform conversion
    if unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Invalid unit. Please enter 'F' or 'C'.")

if __name__ == "__main__":
    temperature_converter()
