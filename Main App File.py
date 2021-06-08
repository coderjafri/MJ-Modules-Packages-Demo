# We need to first call our module "functions.py"

# Just for learning, I will use the 3 ways below :

# First way 

import Functions

# We need to call our function: Functions.find_factorial(x)

# Second way
from Functions import *
# We can use: find_factorial(x)

# Third way :
from Functions import find_factorial

# The factorial of 5 is: 120
print("The factorial of 5 is:", Functions.find_factorial(5))
print("The factorial of 7 is:", Functions.find_factorial(7))


print("The factorial of 8 is:", find_factorial(8))
