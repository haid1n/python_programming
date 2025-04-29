# Imported modules
import tkinter as tk


# Functions for buttons
def first_function():
	print("This is first.")

def second_function():
	print (input_box.get() + input_box.get())


# Create main window
main_window = tk.Tk()

# Give name of window
main_window.title("Temp App")

# Give size of window
main_window.geometry("500x300")


# Create label
label = tk.Label(main_window, text="Tkinter app")

# Add label to window
label.pack()


# Create button
button = tk.Button(main_window, text="Tkinter button", command=first_function)

# Add button to window
button.pack()


# Create entry box
input_box = tk.Entry(main_window)

# Add entry box to window
input_box.pack()

# Take entry and uses it
button_2 = tk.Button(main_window, text="TXT Button", command=second_function)

button_2.pack()


# Keep window open
main_window.mainloop()