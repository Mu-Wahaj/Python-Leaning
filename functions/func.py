#function in pythn like any other language is a block of code which is used to perform a specific task. It is reusable and can be called multiple times in a program. Functions help to break down a large program into smaller, manageable pieces, making it easier to read and maintain.
# Example of a function
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!
greet("Bob")  # Output: Hello, Bob!
# Function with a return value
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8  
# Function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
# Function with variable-length arguments
def sum_all(*args):
    return sum(args)
result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15     
# Function with keyword arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")   
greet("Alice")  # Output: Hello, Alice!
greet("Bob", greeting="Hi")  # Output: Hi, Bob!

def complte_name(first_name, last_name):
    return f"{first_name} {last_name}"

full_name = complte_name("John", last_name="Doe")
print(full_name)  # Output: John Doe

