try:

	with open("file_io/missing_file.txt", "r") as missing_file:

		missing_content = missing_file.read()

		print(missing_content)

except FileNotFoundError:
	print("File Error: The file that you are trying to read is missing or does not exist.")