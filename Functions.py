#A function about math formula "Factorial":

def find_factorial(num=0):

    """
    - accepts a numeric integer value
    - returns the factorial of this value
    """

    count = num
    # We need to keep looping while count still more than 0:
    # either count > 0 or count >= 1
    factorial = 1

    while (count > 0):
       
        # print(count)

        factorial = factorial * count

        count -=1

        # Function should only return the result of the factorial (no print)

        return factorial

# print(find_factorial(5)) # 120

# result = find_factorial (5) # 5 + 4 + 3 + 2 + 1
# print(result)

# You can add more functions if you want