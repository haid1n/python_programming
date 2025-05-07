import tkinter as tk

def area_of_a_circle():
	radius = float(radius_entry.get())

	PI = 3.142

	area = PI * radius * radius

	result.set(f"The area of a circle is {area} square metres")

root = tk.Tk()

root.geometry("400x100")

root.title("Area of a circle")

frame = tk.Frame(master=root)

frame.grid(row=3, column=4, padx=10, pady=10)

radius_label = tk.Label(master=frame, text="RADIUS")

radius_label.grid(row=0, column=0, pady=2)

radius_entry = tk.Entry(master=frame)

radius_entry.grid(row=1, column=0, padx=1)

calculator_button = tk.Button(master=frame, text="CALCULATE", command=area_of_a_circle)

calculator_button.grid(row=0, column=8, padx=10)

result = tk.StringVar()

result.set("AREA")

result_label = tk.Label(master=frame, textvariable=result)

result_label.grid(row=1, column=8)

root.mainloop()