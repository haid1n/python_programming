with open("file_io/log_file.log", "r") as log_file:
	#log_content = log_file.read()

	#print(log_content)

	log_content = log_file.readlines()

for log_message in log_content:
	print(log_message)