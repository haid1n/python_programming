# A function for the common element between two strings
def common_letter(string1, string2):
	elements_of_str1 = set(string1.lower()) # Creates a set of elements in lowercase

	elements_of_str2 = set(string2.lower()) # Creates a set of elements in lowercase

	common_element = elements_of_str1 & elements_of_str2 # Compares both sets and takes the common element in both of them

	return common_element

print(common_letter("Haise", "Dash"))