# Finds missing number using summation
def get_missing_summation(natural_number_list):
	last_number = natural_number_list[-1]

	outcome = last_number * (last_number+1) // 2

	sum_total = sum(natural_number_list)

	print(outcome-sum_total)


# Finds missing numbers using xor
def get_missing_xor(natural_number_list):
	number_of_digits = len(natural_number_list)

	xor_of_numbers = natural_number_list[0]

	for index in range(1, number_of_digits):
		xor_of_numbers = xor_of_numbers ^ natural_number_list[index]
		
	xor_2 = 0

	for index in range(1, number_of_digits+2):
		xor_2 = xor_2 ^ index

	print(xor_of_numbers ^ xor_2)


a = [1, 2, 4, 5, 6, 7, 8, 9]

get_missing_xor(a)