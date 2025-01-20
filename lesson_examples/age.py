year_of_birth = int(input("Enter the year of your birth = "))

current_year = int(input("Enter the current year = "))

age = current_year - year_of_birth

LEGAL_AGE = 18

if age >= LEGAL_AGE:
	print("You are", age, "years old and are eligible to vote.")

else:
	print("You are", age, "years old and are unable to vote.")