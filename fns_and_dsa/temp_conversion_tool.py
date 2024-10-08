# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Global variable for Fahrenheit to Celsius conversion
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Ensure this is defined without spaces

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User interaction and input validation
def get_temperature_input():
    try:
        temp = float(input("Enter the temperature to convert: "))  # Updated prompt
        return temp
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")  # Handle non-numeric input

def main():
    try:
        # Updated prompt for unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            # Convert Celsius to Fahrenheit
            celsius = get_temperature_input()
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F.")

        elif unit == "F":
            # Convert Fahrenheit to Celsius
            fahrenheit = get_temperature_input()
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C.")

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
