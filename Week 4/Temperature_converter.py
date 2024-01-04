import tkinter as tk
from tkinter import Label, Entry, Button

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        value = float(entry_value.get())
        source_unit = entry_source_unit.get().upper()
        target_unit = entry_target_unit.get().upper()

        if source_unit == "C" and target_unit == "F":
            result = celsius_to_fahrenheit(value)
            result_label.config(text=f"{value} Celsius is equal to {result} Fahrenheit.")
        elif source_unit == "F" and target_unit == "C":
            result = fahrenheit_to_celsius(value)
            result_label.config(text=f"{value} Fahrenheit is equal to {result} Celsius.")
        else:
            result_label.config(text="Unsupported units. Please enter C or F for Celsius or Fahrenheit.")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a numeric value.")

# Main window
window = tk.Tk()
window.title("Temperature Converter")

# Widgets
Label(window, text="Enter the temperature value:").pack()
entry_value = Entry(window)
entry_value.pack()

Label(window, text="Enter the source unit (C for Celsius, F for Fahrenheit):").pack()
entry_source_unit = Entry(window)
entry_source_unit.pack()

Label(window, text="Enter the target unit (C for Celsius, F for Fahrenheit):").pack()
entry_target_unit = Entry(window)
entry_target_unit.pack()

convert_button = Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = Label(window, text="")
result_label.pack()

# GUI
window.mainloop()
