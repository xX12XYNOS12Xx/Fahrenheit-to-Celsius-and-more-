sud = input("Celsius or Fahrenheit: ")

if sud == "Celsius".lower():
    celsius = input("Fahrenheit to Celsius: ")
    fahrenheit = int(celsius) * (9/5) + 32
    print("Fahrenheit:", fahrenheit)
elif sud == "Fahrenheit".lower():
    fahrenheit = input("Celsius to Fahrenheit: ")
    celsius = (int(fahrenheit) - 32) * (5/9)
    print("Celsius:", celsius)
else:
    print("Invalid input. Please enter 'Celsius' or 'Fahrenheit'.")
