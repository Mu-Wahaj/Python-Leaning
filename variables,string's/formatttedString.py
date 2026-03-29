# String Formatting in Python
# In Python, you can format strings using various methods. Here are some common ways to format strings:     


first_name="John"
last_name="Doe"
message1 = first_name + " [" + last_name + "] is learning Python."
print(message1)  
# message2 = "Hello, {} {}. Welcome to the world of Python.".
# format(first_name, last_name)
# print(message2) 
message3=f'Hello, {first_name} [{last_name}]. Welcome to the world of Python.'
print(message3)  

# String Method/functions in Python
course = 'Python Programming'
print(len(course))  # Length of the string
print(course.upper())  # Convert to uppercase
print(course.lower())  # Convert to lowercase
print(course.title())  # Convert to title case
print(course.strip())  # Remove leading and trailing whitespace
print(course.replace('Python', 'Java'))  # Replace a substring
print(course.find('Programming'))  # Find the index of a substring
print(course.split())  # Split the string into a list
print(course.startswith('Python'))  # Check if the string starts with a substring
print(course.endswith('Programming'))  # Check if the string ends with a substring
print(course.count('o'))  # Count occurrences of a substring
course = course.replace('Python', 'Java')  # This does not change the original string, it returns a new string
print(course)  # The original string remains unchanged
print('Python' in course)  # Check if a substring is in the string
print('Java' not in course)  # Check if a substring is not in the string

