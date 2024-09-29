CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):

    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):

    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_temperature_input():

    try:
        temp = float(input("Enter the temperature: ").strip())
        unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        return temp, unit

    except ValueError as e:
        raise ValueError("Invalid temperature. Please enter a numeric value.") from e

def main():
    try:
        temperature, unit = get_temperature_input()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")

    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()
