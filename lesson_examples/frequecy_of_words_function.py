# Function for counting the number of times a word appears in a string
def word_frequency(string):
	word_list = string.split() # Splits the string into elements

	string_dictionary = {}

# Checks the number of occurences of a string element
	for element in word_list:
		if element not in string_dictionary.keys(): # Assigns a value of zero to a newly formed key
			string_dictionary[element] = 0

		string_dictionary[element] = string_dictionary[element] + 1 # Adds one to the key picked

	return string_dictionary

