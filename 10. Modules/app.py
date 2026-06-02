#modules are like multifiling in other programming languages, they are a way to organize and reuse code in Python. A module is simply a file containing Python code that defines functions, classes, or variables. You can import a module into another Python file to use the code defined in that module. Here's an example of how to create and use a module in Python:  


import converter
# Now you can use the functions defined in the converter module
celsius = 25
fahrenheit = converter.celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# another way using from keyword to import specific functions from the module
from converter import dollars_to_rupees
money_in_dollars = 100
money_in_rupees = dollars_to_rupees(money_in_dollars)
print(f"{money_in_dollars} dollars is equal to {money_in_rupees} rupees.")

# exercise to find the maximum value in a list using a function from the converter module
max_value = converter.find_max([1, 2, 3, 4, 5])
print(f"The maximum value in the list is: {max_value}")



#there are many built-in modules in Python that provide a wide range of functionality, such as math, random, datetime, and os. You can also create your own custom modules to organize your code and make it reusable across different projects. we can find the list of built-in modules in the Python documentation or by using the help() function in Python. For example, to see a list of all built-in modules, you can run the following code:
import sys
print(sys.builtin_module_names)


# or go the Python documentation and search for "python 3 modules index" to find the list of built-in modules.


#example of using the random module to generate a random number between 1 and 10
import random
random_number = random.randint(1, 10)
print(f"The random number generated is: {random_number}")



def roll_dice():
    return random.randint(1, 6)
dice_result = roll_dice()
print(f"You rolled a {dice_result} on the dice.")

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"You rolled a {die1} and a {die2} on the dice.")
    return die1,die2

dice= roll_two_dice()
print(dice)