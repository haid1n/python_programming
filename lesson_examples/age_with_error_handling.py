try:
	year_of_birth = int(input("Enter the year of your birth = "))

	current_year = int(input("Enter the current year = "))

	age = current_year - year_of_birth

	LEGAL_AGE = 18

	if age >= LEGAL_AGE:
		print("You are", age, "years old and are eligible to vote.")

	elif age <= 0:
		raise ValueError("This age is not acceptable. Try again.")

	else:
		print("You are", age, "years old and are unable to vote.")

except Exception as a:
	print(f"Error : {a}")