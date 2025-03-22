file = open("file_io/sample.txt", "r")

# full_content = file.read()

# first_line = file.readline()

# second_line = file.readline()

# third_line = file.readline()

lines = file.readlines()

print(lines)

file.close()