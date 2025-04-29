# Convert list to dictionary
def list_to_dictionary():
	keys = [1,2,3]

	values = ["one", "two", "three"]

	result = dict(zip(values, keys)) # Creates a key-value dictionary

	print(result)

# Converts a dictionary to a tuple
def dict_to_tuple():
	x = {'one': 1, 'two': 2, 'three': 3}

	for pairs in x.items(): # Creates a number of tuples with distinct key value pair
		print(pairs)

dict_to_tuple()