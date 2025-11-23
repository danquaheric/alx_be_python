# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    elif unit == "F":
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    else:
        raise ValueError("Invalid temperature unit. Please enter C or F.")

if __name__ == "__main__":
    main()
