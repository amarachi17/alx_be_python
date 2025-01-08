# Defining two global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 #Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 # Factor to convert Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    # Convert a temperature from Fahrenheit to Celsius
    # global FAHRENHEIT_TO_CELSIUS_FACTOR
    return round((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR, 2)
    # return round(celsius, 2)

def convert_to_fahrenheit(celsius):
    # Convert a temperature from Celsius to Fahrenheit.
    # global CELSIUS_TO_FAHRENHEIT_FACTOR
    return round ((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32, 2)
    # return round(fahrenheit, 2)

def main():
    print("Temperature Conversion Tool")
    
    # Get the user input
    try: 
        temperature = float(input("Enter the temperature to convert: "))
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()
    
    # Perform the conversion
    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equivalent to {converted}°F.")
    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is equivalent to {converted}°C.")
    else: 
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit")  
        
# Run the script
if __name__ == "__main__":
    main()
    