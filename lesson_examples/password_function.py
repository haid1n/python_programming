import random

import string

# Store the numeric values
NUMBERS = "0123456789" 

# Store symbols
SYMBOLS = "!@#$%" 

# Store all uppercase letters
CAPITAL_LETTERS = string.ascii_uppercase

# Store all lowercase letters
SMALL_LETTERS = string.ascii_lowercase

# Store all alphanumeric characters (ie alphabets, numbers and symbols)
ALL_CHARACTERS = NUMBERS + SYMBOLS + CAPITAL_LETTERS + SMALL_LETTERS

# Function for generating password
def generate_password(length):
	# For setting password length to twelve if it is below 12
	if length < 12:
		length = 12

	# Store random capital letters
	random_capital_letter = random.choice(CAPITAL_LETTERS)

 	# Store random small letters
	random_small_letter = random.choice(SMALL_LETTERS)

	# Store random numbers
	random_number = NUMBERS[random.randint(0, 9)] 

	# Store random symbols
	random_symbol = SYMBOLS[random.randint(0, 4)] 
	
	# Store randomly generated password containing alphabets, numbers and symbols
	passcode = [random_capital_letter, random_small_letter, random_number, random_symbol]

	# Creates password according to length specified
	while len(passcode) < length:		
		random_character = random.choice(ALL_CHARACTERS) # Generate random password using all characters

	# Add more characters to the password list
		passcode.append(random_character)
		 
	random.shuffle(passcode)

	# Join a list of strings as a single string
	string_passcode = "".join(passcode) 
	return string_passcode

password = generate_password(20)

print(password)