class Dog:
	def sound(self):
		return "Bark"

class Cat:
	def sound(self):
		return "Meow"

# Function that works with different objects
def make_sound(animal):
	print(animal.sound())

dog_1 = Dog()

cat_1 = Cat()

make_sound(animal=dog_1)

make_sound(animal=cat_1)