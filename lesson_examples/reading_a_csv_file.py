import csv

with open("file_io/employee_data.csv", "r") as csv_file:
	csv_reader = csv.reader(csv_file)

	for row in csv_reader:
		print(row)
