import math

def solve_quadratic_equation(a: float, b: float, c: float):
	"""
	Solves a quadratic equation of the form ax + bx + c = 0

	Parameters:
		a (float): Coefficient of x

		b (float): Coefficient of b

		c (float): Coefficient of c

	Returns:
		tuple: A tuple of two real or complex roots

	"""

	discriminant = b ** 2 - 4 * a * c

	if discriminant >= 0:
		root1 = (-b + math.sqrt(discriminant)) / (2 * a)

		root2 = (-b - math.sqrt(discriminant)) / (2 * a)

	else:
		real_part = -b / (2 * a)

		imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)

		root1 = complex(real_part, imaginary_part)

		root2 = comples(real_part, -imaginary_part)