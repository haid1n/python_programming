# Import Libraries
from datetime import datetime

# Set Constant(s)
TODAYS_DATE = datetime.today().date()


# Take Inputs
first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

birth_date = input("Enter your birthdate in this format (yyyy-mm-dd), Example [2000-12-25]: \n>>>")


# Handle/Control Invalid Inputs
if not first_name.isalpha() or not last_name.isalpha():

	raise ValueError("First name and last name must be alphabets")

if not isinstance(birth_date, str):

	raise TypeError("Birthdate must be a string value.")


# Transform inputs
full_name = f"{first_name} {last_name}".title()

user_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

user_age = TODAYS_DATE.year - user_birth_date.year


# Set output message
output_message = f"The user's name is {full_name}.\nThe user's age is {user_age}"


# Display output message
print(output_message)


# Set user info log
user_info_log = f"USER_NAME: {full_name}, USER_BIRTH_DATE: {user_birth_date}, USER_AGE: {user_age}"


# Write user's details to a file
with open("file_io/user_info_log.txt", "w") as info_log_file:
	info_log_file.write(user_info_log)
