def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/93

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    choice = int(input("Enter your choice (1-6): "))
    temperature = float(input("Enter the temperature value: "))
    
    if choice == 1:
        print(f"{temperature}°C = {celsius_to_fahrenheit(temperature):.2f}°F")
    elif choice == 2:
        print(f"{temperature}°C = {celsius_to_kelvin(temperature):.2f}K")
    elif choice == 3:
        print(f"{temperature}°F = {fahrenheit_to_celsius(temperature):.2f}°C")
    elif choice == 4:
        print(f"{temperature}°F = {fahrenheit_to_kelvin(temperature):.2f}K")
    elif choice == 5:
        print(f"{temperature}K = {kelvin_to_celsius(temperature):.2f}°C")
    elif choice == 6:
        print(f"{temperature}K = {kelvin_to_fahrenheit(temperature):.2f}°F")
    else:
        print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
