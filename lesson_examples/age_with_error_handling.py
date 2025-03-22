try:
	year_of_birth = int(input("Enter the year of your birth = "))

	current_year = int(input("Enter the current year = "))

	if year_of_birth <= 0 or current_year <= 0:
		raise ValueError("The year of birth or current year's value is incorrect.")

	age = current_year - year_of_birth

	LEGAL_AGE = 18

	if age >= LEGAL_AGE:
		print("You are", age, "years old and are eligible to vote.")

	else:
		print("You are", age, "years old and are unable to vote.")

except Exception as error_message:
	print(f"Error : {error_message}")