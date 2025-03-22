try:
	mass_of_the_first_body = float(input("Enter the mass of the first body = "))

	mass_of_the_second_body = float(input("Enter the mass of the second body = "))

	distance_seperating_the_bodies = float(input("Enter the distance seperating the two bodies = "))

	if mass_of_the_first_body <= 0 or mass_of_the_second_body <= 0 or distance_seperating_the_two_body <= 0:
		raise ValueError("The value for the mass of the first body or mass of the second body or distance separating the bodies is not accepted")

	GRAVITATIONAL_CONSTANT = 6.67 * 0.00000000001

	gravitation	= GRAVITATIONAL_CONSTANT * mass_of_the_first_body * mass_of_the_second_body / distance_seperating_the_bodies * distance_seperating_the_bodies

	print("The force of gravity between the two bodies =", gravitation)

except Exception as error_message:
	print(f"Error : {error_messages }")

