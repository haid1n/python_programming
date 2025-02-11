try:
	mass_of_the_first_body = float(input("Enter the mass of the first body = "))

	mass_of_the_second_body = float(input("Enter the mass of the second body = "))

	distance_seperating_the_bodies = float(input("Enter the distance seperating the two bodies = "))

	GRAVITATIONAL_CONSTANT = 6.67 * 0.00000000001

	gravitation	= GRAVITATIONAL_CONSTANT * mass_of_the_first_body * mass_of_the_second_body / distance_seperating_the_bodies * distance_seperating_the_bodies

	if gravitation <= 0:
		raise ValueError("Force of gravity is not accepted")

	else:
		print("The force of gravity between the two bodies =", gravitation)

except Exception as z:
	print(f"Error : {z}")

