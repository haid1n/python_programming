import csv

new_employee_data = [4, "Justin", 28, "Pharmacy"]

with open("file_io/employee_data.csv", "a", newline="") as csv_file:
	writer = csv.writer(csv_file)

	writer.writerow(new_employee_data)

print("New employee data added.")