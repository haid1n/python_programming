def body_mass_index(mass, height):
	BMI = mass / height * height

	UNDER_WEIGHT_TRESHOLD = 18.5

	HEALTHY_MINIMUM_TRESHOLD = 18.6

	HEALTHY_MAXIMUM_TRESHOLD = 24.9

	OVER_WEIGHT_MINIMUM_TRESHOLD = 25

	OVER_WEIGHT_MAXIMUM_TRESHOLD = 29.9

	OBESE_TRESHOLD = 30

	if 0 < BMI < UNDER_WEIGHT_TRESHOLD:
		print("You are underweight")

	elif BMI >= HEALTHY_MINIMUM_TRESHOLD and BMI <= HEALTHY_MAXIMUM_TRESHOLD:
		print("You are healthy")

	elif BMI >= OVER_WEIGHT_MAXIMUM_TRESHOLD and BMI <= OVER_WEIGHT_MAXIMUM_TRESHOLD:
		print("You are overweight")

	elif BMI > OBESE_TRESHOLD:
 		print("You are obese")

	if BMI <= 0:
		raise ValueError("An irregular value")

"""
	else:
 		print("The lowest possible BMI is 0.\nYou have a BMI of: ", BMI)
"""	
try:
	body_mass_index(-78, 45)

except Exception as a:
	print(f"Error : {a}")






 		