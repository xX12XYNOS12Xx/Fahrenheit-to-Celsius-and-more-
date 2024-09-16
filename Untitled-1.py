import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    temp = entry.get()
    try:
        temp = float(temp)
        if var.get() == "Celsius":
            fahrenheit = temp * (9/5) + 32
            result_label.config(text=f"{temp}°C is {fahrenheit:.2f}°F")
        elif var.get() == "Fahrenheit":
            celsius = (temp - 32) * (5/9)
            result_label.config(text=f"{temp}°F is {celsius:.2f}°C")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create a label and entry for temperature input
entry_label = tk.Label(root, text="Enter temperature:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create radio buttons for Celsius and Fahrenheit
var = tk.StringVar(value="Celsius")
celsius_radio = tk.Radiobutton(root, text="Celsius", variable=var, value="Celsius")
celsius_radio.pack()
fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit", variable=var, value="Fahrenheit")
fahrenheit_radio.pack()

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
