import csv

with open("file_io/employee_data.csv", "r") as csv_file:
	csv_content = csv.DictReader(csv_file)

	for row in csv_file:
		print(row)