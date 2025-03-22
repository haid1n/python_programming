class Car:
	# Constructor method
	def __init__(self, brand, model, year):
		# Instance attributes
		self.brand = brand

		self.model = model

		self.year = year

	# Method to print car details
	def display_info(self):
		print(f"{self.year} {self.brand} {self.model}")

car_object = Car(brand="Toyota", model="Corolla", year=2008)

car_object.display_info()