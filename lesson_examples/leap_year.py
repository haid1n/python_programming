year = int(input("Enter the year = "))

is_leap_year = True

outcome_1 = year % 4 

outcome_2 = year % 100

for x in range(1):
	if outcome_1 != outcome_2:
		if outcome_1 != 0:
			break

		is_leap_year = False

for n in range(1):
	if outcome_1 == outcome_2:
		if outcome_1 != 0:
			break 	

		elif year % 400 == 0:
			print("It's a leap year.") 

		else:
			print("It's not a leap year")

if is_leap_year == False:
	print("It's a leap year")

elif outcome_1 != 0:
	print("It's not a leap year")