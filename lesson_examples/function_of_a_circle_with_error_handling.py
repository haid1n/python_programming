def area_of_a_circle(radius):
	PI = 3.142

	area = PI * radius * radius

	return area

try:
	circle = area_of_a_circle(-65)

	print(circle)

except Exception as undefined:
	print(f"Error : {undefined}")