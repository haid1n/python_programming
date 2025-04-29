# Imported module
import tkinter as tk


# Function for converting farenheit to celsius
def farenheit_to_celsius():
	temperature_in_farenheit = float(farenheit_entry.get())

	difference_in_parenthesis = temperature_in_farenheit - 32

	product_of_parenthesis = 5 * difference_in_parenthesis

	temperature_in_degree_celsius =  product_of_parenthesis / 9

	result.set(f"The temperature reading in degree celsius is {temperature_in_degree_celsius}")


# Create main window
root = tk.Tk()

# Set dimension for window
root.geometry("400x100")

# Generate title for window
root.title("Farenheit to degree celsius")


# Create frame
frame = tk.Frame(master=root)

frame.grid(row=3, column=4, padx=10, pady=10)


# Create farenheit label
farenheit_label = tk.Label(master=frame, text="FARENHEIT")

farenheit_label.grid(row=0, column=0, pady=2)


# Create entry for Farenheit
farenheit_entry = tk.Entry(master=frame)

farenheit_entry.grid(row=1, column=0, padx=1)



# Create button for calculation
calculator_button = tk.Button(master=frame, text="CALCULATE", command=farenheit_to_celsius)

calculator_button.grid(row=0, column=3, padx=10)


# Create string object to hold text
result = tk.StringVar()

# Give out the text
result.set("CELSIUS")


# Give the result
result_label = tk.Label(master=frame, textvariable=result)

result_label.grid(row=1, column=3)


# Keep window open
root.mainloop()
