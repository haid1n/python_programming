# Imported module
import tkinter as tk


# Function for density of a substance
def density_of_a_substance():
	mass = float(mass_entry.get())

	volume = float(volume_entry.get())

	density = mass / volume

	result.set(f"The density of a substance is {density} kilograms per metre cube")



# Create main window
root = tk.Tk()

# Set dimension for window
root.geometry("590x100")

# Generate title for window
root.title("Density of a substance")


# Create frame
frame = tk.Frame(master=root)

frame.grid(row=3, column=4, padx=10, pady=10)


# Create mass label
mass_label = tk.Label(master=frame, text="MASS")

mass_label.grid(row=0, column=0, pady=2)

# Create volume label
volume_label = tk.Label(master=frame, text="VOLUME")

volume_label.grid(row=0, column=5, pady=2)



# Create entry for mass
mass_entry = tk.Entry(master=frame)

mass_entry.grid(row=1, column=0, padx=1)

# Create entry for volume
volume_entry = tk.Entry(master=frame)

volume_entry.grid(row=1, column=5, padx=1)



# Create button for calculation
calculator_button = tk.Button(master=frame, text="CALCULATE", command=density_of_a_substance)

calculator_button.grid(row=0, column=10, padx=10)


# Create string object to hold text
result = tk.StringVar()

# Give out the text
result.set("DENSITY")


# Give the result
result_label = tk.Label(master=frame, textvariable=result)

result_label.grid(row=1, column=10)


# Keep window open
root.mainloop()