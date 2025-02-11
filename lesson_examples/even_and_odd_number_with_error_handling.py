try:
	natural_number = int(input("Enter any natural number :"))

	outcome = natural_number % 2

	if outcome == 0:
		print("The number is an even number")

	else:
		print("The number is an odd number")

except Exception as a:
	print(f"Error : {a}")
