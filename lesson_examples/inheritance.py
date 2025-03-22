class Vehicle: # Parent class
	def __init__(self, brand, year):
		self.brand = brand

		self.year = year

	def display_info(self):
		print(f"Vehicle : {self.brand} {self.year}")

class Car(Vehicle): # Child class (inherits from Vehicle)
	def __init__(self, brand, year, model):
		super().__init__(brand, year) # Call parent class constructor

		self.model = model

	def display_car(self):
		print(f"Car : {self.year} {self.brand} {self.model}")

car_1 = Car(brand="Toyota", year=2006, model="Corolla")

print(car_1.display_car())

print(car_1.display_info())