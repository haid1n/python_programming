## Imported modules ##
from os import listdir

from os.path import isfile , join


# Store filepath
filepath = r"C:\Users\chari plus\Documents"

# Create list of files
file_list = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Give the extension of the file
for file in file_list:
	file_components = file.split(".")

	file_extension = file_components[-1]

	print(file_extension)