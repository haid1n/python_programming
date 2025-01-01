coefficient_of_friction = float(input("Give the coefficient of friction : "))

mass = float(input("Enter the mass of the object = "))

ACCELERATION_DUE_TO_GRAVITY = 10

friction = coefficient_of_friction  * mass * ACCELERATION_DUE_TO_GRAVITY

print("The frictional force of a bicycle descending a hill is", friction)
