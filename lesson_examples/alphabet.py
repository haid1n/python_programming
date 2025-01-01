letter = input("Enter a letter of the alphabet :")

if letter == "a" or letter == "e" or \
letter == "i" or letter == "o" or \
letter == "u":
	print("The letter you is a vowel")
elif letter == "y" or letter == "h":
	print("The letter you entered is a consonant and sometimes a vowel")

else:
	print("The letter you entered is a consonant")
