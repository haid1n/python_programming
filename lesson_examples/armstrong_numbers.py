# For displaying armstrong numbers
for value in range(100):
	number = value

	result = 0

	number_of_single_digits = len(str(value)) # Counts the number of single digits when given whole numbers

# Each individual digit is given an exponent and their individual products are summed together
	while (value != 0):
		digit = value % 10 # Finds the remainder for each new dividend brought

		result += digit ** number_of_single_digits

		value = value // 10 # Gives a dividend after each loop

	if number == result:
		print(result)