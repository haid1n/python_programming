# Imported module
import tkinter as tk


# Function for converting celsius to kelvin
def celsius_to_kelvin():
	celsius = celsius.get()

	UPPER_FIXED_POINT = 273.16

	kelvin = celsius - UPPER_FIXED_POINT


# Main window
root = tk.Tk()


# Title
root.title("Degree celsius to Kelvin")


# Window space
root.geometry("300x200")


# Window frame
frame = tk.Frame(master=root)

frame.grid()


# Textbox
celsius = tk.Text(master=frame)

celsius.grid()


# Buttton
calculator_button = tk.Button(master=frame, text="CALCULATE", command=celsius_to_kelvin)

calculator_button.grid()


# Labels
celsius_label = tk.Label(master=frame, text="CELSIUS")

celsius.grid()

# Create string object to hold text
result = StringVar()

# Give out text
result.set("Kelvin")

kelvin_label = tk.Label(master=frame, textvariable=result)