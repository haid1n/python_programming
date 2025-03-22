"""
Collection of functions for dimensions

Functions:
----------
area,
	Function to calculate the area of an object.

perimeter,
	Function to calculate the perimeter of an object.

volume,
	Function to calculate the volume of an object.

surface area,
	Function to calculate the surface area of an object.
"""

def area(length: int, width: int) -> int:
	"""
	Function to calculate the area of an object.

	Parameters:
	-----------
	length: integer,
		First number used for calculating area.

	width: integer
		Second number used for calculating area.

	Return:
	-------
	output: integer,
		The product of two numbers.

	Example:
	--------
	>>> area(length=5, width=4)
	>>> 20

	>>> area(5, 4)
	>>> 20

	>>> area(width=4, length=5)
	>>> 20
	"""

	area_of_an_object = length * width

	return area_of_an_object

def perimeter(length: int, width: int) -> int:
	"""
	Function to calculate the perimeter of an object.

	Parameters:
	-----------
	length: integer,
		First & Third number used for calculating perimeter.

	width: integer,
		Second & Fourth number used for calculating perimeter.

	Return:
	-------
	output: float,
		The sum of the numbers.

	Example:
	--------
	>>> perimeter(length=3, width=2)
	>>> 10

	>>> perimeter(3, 2)
	>>> 10

	>>> perimeter(width=2, length=3)
	>>> 10
	"""

	perimeter_of_object = length + width + length + width

	return perimeter_of_object

def volume(length, width, height):
	"""
	Function to calculate the volume of an object.

	Parameters:
	-----------
	length: integer,
		First number used for the volume.

	width: integer,
		Second number used for the volume.

	height: integer,
		Third number used for the volume.

	Return:
	-------
	output: integer,
		The product of the numbers.

	Example:
	--------
	>>> volume(length=4, width=5, height=10)
	>>> 200

	>>> volume(4, 5, 10)
	>>> 200

	>>> volume(width=5, height=10, length=4)
	>>> 200
	"""

	volume_of_object = length * width * height

	return volume_of_object

def surface_area(length, width, height):
	"""
	Function to calculate the surface area of an objedt

	Parameters:
    -----------
    length: integer,
    	First number used for surface area.

    width: integer,
    	Second number used for surface area.

    height: integer,
    	Third number used for surface area.

    Return:
    -------
    output: integer,
    	The sum total.

    Example:
    --------
    >>> surface_area(length=4, width=5, height=6)
    >>> 148

    >>> surface_area(4, 5, 6)
    >>> 148

    >>> surface_area(height=6, length=4, width=5)
    >>> 148
	"""
	
	surface_area_of_object = 2 * length * width + 2 * length * height + 2 * height * width

	return surface_area_of_object

print(surface_area.__doc__)