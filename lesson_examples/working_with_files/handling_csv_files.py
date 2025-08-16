import csv

employee_data = [
	["ID", "Name", "Age", "Department"],
	[1, "Alice", 30, "HR"],
	[2, "Bob", 25, "IT"],
	[3, "Trevor", 27, "Finance"],
]

with open("file_io/employee_data.csv", "w", newline="") as csv_file:
	writer = csv.writer(csv_file)

	writer.writerows(employee_data)

print("csv file created successfully.")