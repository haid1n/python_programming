"""
Collection of simple math functions

Functions:
---------
add,
	Function to add two numbers.

subtract,
	Function to subtract two numbers.

divide,
	Function to divide two numbers.

multiply, 
	Function to multiply two numbers.
"""

def add(num_1: float, num_2: float) -> float:
	"""

	Function to add two numbers.
 
	Parameters:
	---------- 
	num_1: float,
		First number for the addition operation

	num_2: float,
		Second number for the addition operation

	Return Type:
	----------- 
	output: float,
		The sum of two numbers

	Example:
	-------
	>>> add(num_1=10, num_2=5)
	>>> 15

	>>> add(10, 5)
	>>> 15

	>>> add(num_2=5, num_1=10)
	>>> 15
	"""

	output: float = num_1 + num_2

	return output

def subtract(num_1: float, num_2: float) -> float:
	"""
	Function to subtract two numbers

	Parameters:
	---------- 
	num_1: float,
		First number for the subtraction

	num_2: float,
		Second number for subtraction

	Return Type:
	----------- 
	output: float,
		The difference between two numbers.

	Example:
	-------
	>>> subtract(num_1=10, num_2=5)
	>>> 10

	>>> subtract(10, 5)
	>>> 10

	>>> subtract(num_2=5, num_1=10)
	>>> 10
	"""

	output: float = num_1 + num_2

	return output

def divide(num_1: float, num_2: float) -> float:
	"""
	Function to divide two numbers.

	Parameters:
	---------- 
	num_1: float,
		The dividend

	num_2: float,
		The divisor

	Return Type:
	-----------
	output: float,
		The quotient

	Example:
	------- 
	>>> divide(num_1=10, num_2=5)
	>>> 2

	>>> divide(10, 5)
	>>> 2

	>>> divide(num_2=10, num_1=5)
	>>> 2
	"""

	output: float = num_1 / num_2

	return output

def multiply(num_1: float, num_2: float) -> float:
	"""
	Function to multiply two numbers.

	Parameters:
	---------- 
	num_1: float,
		First number for the multiplication operation

	num_2: float,
		Second number for the multiplication operation

	Return Type:
	----------- 
	output: float,
		The product of two numbers.

	Example:
	------- 
	>>> multiply(num_1=10, num_2=5)
	>>> 50

	>>> multiply(10, 5)
	>>> 50

	>>> multiply(num_2=5, num_1=5)
	>>> 50
	"""

	output: float = num_1 * num_2

	return output
