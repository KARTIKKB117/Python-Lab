choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()
temp = float(input("Enter temperature: "))

if choice == "C":
    converted = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {converted:.2f}°C")
else:
    converted = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {converted:.2f}°F")
