class BankAccount:
	def __init__(self, balance):
		self.__balance = balance # Private attribute

	def deposit(self, amount):
		self.__balance += amount
		print(f"Deposited : ${amount}")

	def get_balance(self):
		return self.__balance # Access private variable through a method

trustfund = BankAccount(balance=4000)

trustfund.deposit(amount=1200)

# print(trustfund.__balance)

print(trustfund.get_balance())