def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.strip().lower()
    to_scale = to_scale.strip().lower()
    
    if from_scale == "celsius":
        if to_scale == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "kelvin":
            return celsius_to_kelvin(value)
    elif from_scale == "fahrenheit":
        if to_scale == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_scale == "kelvin":
        if to_scale == "celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "fahrenheit":
            return kelvin_to_fahrenheit(value)
    return value

def main():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return

    from_scale = input("Enter the current scale (Celsius, Fahrenheit, Kelvin): ")
    to_scale = input("Enter the target scale (Celsius, Fahrenheit, Kelvin): ")
    
    if from_scale.lower() not in ["celsius", "fahrenheit", "kelvin"]:
        print("Invalid input scale. Please enter one of: Celsius, Fahrenheit, Kelvin.")
        return
    
    if to_scale.lower() not in ["celsius", "fahrenheit", "kelvin"]:
        print("Invalid target scale. Please enter one of: Celsius, Fahrenheit, Kelvin.")
        return

    converted_value = convert_temperature(value, from_scale, to_scale)
    print(f"{value} {from_scale.capitalize()} is equal to {converted_value:.2f} {to_scale.capitalize()}")

if __name__ == "__main__":
    main()
