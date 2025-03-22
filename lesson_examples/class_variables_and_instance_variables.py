class Employee:
	company = "TechCorp" # Class variable (same for all employees)

	def __init__(self, name, salary):
		self.name = name # Instance variable (unique for all objects)

		self.salary = salary

employee_1 = Employee(name="Johnathan", salary=60000)

employee_2 = Employee(name="Rebecca", salary=50000)

print(employee_1.name)

print(employee_2.name)

print(employee_1.company)

print(employee_2.company)


employee_1.name = "Kent"

print(employee_1.name)

print(employee_2.name)


Employee.company = "StockCorp"


print(employee_1.company)

print(employee_2.company)