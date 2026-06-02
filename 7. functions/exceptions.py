## exceptions in python are errors that occur during the execution of a program. They can be caused by various factors, such as invalid input, division by zero, or trying to access a non-existent file. When an exception occurs, the normal flow of the program is interrupted, and an error message is displayed. However, Python provides a way to handle exceptions using try-except blocks, allowing you to gracefully handle errors and prevent your program from crashing. Here's an example of how to use try-except blocks to handle exceptions:
try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
    
    ## now here if user enters any invalid data athatis not a numerical value, it will raise a ValueError. If the user enters zero as the second number, it will raise a ZeroDivisionError. By using try-except blocks, we can catch these exceptions and provide appropriate error messages to the user instead of crashing the program.
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
    
    ### other excepton errors include:
# FileNotFoundError: Raised when trying to access a file that does not exist.
# IndexError: Raised when trying to access an index that is out of range in a list or other sequence.
# KeyError: Raised when trying to access a key that does not exist in a dictionary.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# Example of handling a FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The specified file was not found.")
    
    ## you can also use a generic except block to catch any type of exception that may occur. However, it's generally recommended to catch specific exceptions to provide more informative error messages and handle different types of errors appropriately.
try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
    ## In this example, the generic except block catches any exception that may occur and prints a message along with the exception details. However, it's important to use this approach with caution, as it can make it harder to identify and debug specific issues in your code.
    
## you can also use the finally block in conjunction with try-except to ensure that certain code is executed regardless of whether an exception occurred or not. The code inside the finally block will always be executed, even if an exception was raised and caught in the except block.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This block will always be executed, regardless of exceptions.")
    
    ## In this example, the finally block will execute after the try and except blocks, ensuring that the message "This block will always be executed, regardless of exceptions." is printed regardless of whether an exception occurred or not. This can be useful for cleaning up resources, closing files, or performing any necessary finalization tasks in your code.
    

