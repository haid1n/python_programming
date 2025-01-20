year = int(input("Enter the year = "))

outcome_1 = year % 4

outcome_2 = year % 100
if outcome_1 == outcome_2 or outcome_1 != outcome_2:
	if outcome_1 != 0:
		print("It's not a leap year.")

	elif outcome_2 == year % 400 or outcome_1 != outcome_2:
		print("It's a leap year.")

	else:
		print("It's not a leap year.")