try:
	number = int(input("Enter a number = "))

	is_prime = True

	if number < 2:
		is_prime = False

	else:
		for x in range(2, int(number ** 0.5) + 1):

			if number % x == 0:
				is_prime = False
				break

	if is_prime == True:
		print("The number", number, "is a prime number.")

	else:
		print("The number", number, "is not a prime number")

except Exception as a:
	print(f"Error : {a}")