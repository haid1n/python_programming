with open("file_io/sample.txt", "r") as file:
	#full_content = file.read()

	first_line = file.readline()

	#print(full_content)

	print(first_line)