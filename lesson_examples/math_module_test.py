import modules
from modules import math_functions
from modules.math_functions import subtract

difference = subtract(65, 43)

print(subtract.__doc__)

print(difference)

sum_ = math_functions.add(6, 7)

print(sum_)

print(math_functions.add.__doc__)

division = modules.math_functions.divide(6, 3)

print(division)

print(modules.math_functions.divide.__doc__)
