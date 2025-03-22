def body_mass_index(mass, height):
	try:
		if not str(mass).isnumeric() or not str(height).isnumeric():
			raise TypeError("The mass or height value is not numeric")

		if mass <= 0 or height <= 0:
			raise ValueError("The value is less than or equal to zero and therefore not accepted")

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

	except Exception as error_message:
		print(f"Error : {error_message}")

"""
	else:
 		print("The lowest possible BMI is 0.\nYou have a BMI of: ", BMI)
"""

body_mass_index(7, 3)







 		