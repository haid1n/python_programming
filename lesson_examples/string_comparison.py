def compare(string1, string2):
	#Checks wether the first string is in the second string
	if string1 in string2:
		print (string1, "is a substring of", string2)

	#Does the vice versa
	if string2 in string1:
		print (string2, "is a substring of", string1)

	#Checks whether string1 is the same as the string2
	if string1 == string2:
		print (string1, "equals", string2)

	#Compares them using the ASCII
	elif string1 > string2:
		print (string1, "comes after", string2)

	else:
		print(string1, "comes before", string2)

compare("banana", "banana")