try:
	mass = float(input("Enter the mass of the substance = "))

	volume = float(input("Enter the volume of the substance = "))

	density = mass / volume

	if density <= 0:
		raise ValueError("The substance's density is abnormal and therefore rejected")

	else:
		print("The density of the substance is", density)

except Exception as q:
	print(f"Error : {q}")