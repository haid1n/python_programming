number = int(input("Enter a natural number from 1 to 100 = "))

if number < 0 or number > 100:
	print("It's not within the range.")

elif number == 2 or number == 3 or number == 5 or \
number == 7 or number == 11 or number == 13 or \
number == 17 or number == 19 or number == 23 or \
number == 29 or number == 31 or number == 37 or \
number == 41 or number == 43 or number == 47 or \
number == 53 or number == 59 or number == 61 or \
number == 67 or number == 71 or number == 79 or \
number == 83 or number == 89 or number == 97:
	print("The number is a prime number.")

else:
	print("The number is not a prime number.")

