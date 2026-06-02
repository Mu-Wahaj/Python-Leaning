# package is a collection of modules that are organized in a directory hierarchy. It allows you to organize your code into logical groups and makes it easier to manage and maintain. In Python, a package is created by including an __init__.py file in a directory. This file can be empty or contain initialization code for the package. The __init__.py file is executed when the package is imported, and it can be used to define the public interface of the package or to perform any necessary setup tasks. By using packages, you can create a well-structured and modular codebase that is easier to navigate and maintain.

import shipping 
# Now you can use the shipping_cost function defined in the shipping module
weight = 10  # weight in kilograms
distance = 100  # distance in kilometers
cost = shipping.shipping_cost(weight, distance)
print(f"The shipping cost for {weight} kg over {distance} km is: ${cost:.2f}")


#it is also possible to import specific functions from a module using the from keyword. This allows you to use the function directly without having to prefix it with the module name. Here's an example of how to import a specific function from the shipping module 
# it is bassically comapnents like in react where we can import specific components from a file instead of importing the whole file.
from shipping import shipping_cost
# Now you can use the shipping_cost function directly without the module prefix
weight = 5  # weight in kilograms
distance = 50  # distance in kilometers
cost = shipping_cost(weight, distance)
print(f"The shipping cost for {weight} kg over {distance} km is: ${cost:.2f}")

