#logical opertaor in python are very much like logical opertaor in other programming language, they are used to combine multiple conditions and return a boolean value (True or False) based on the evaluation of those conditions. The three main logical operators in python are:
# and: returns True if both conditions are true, otherwise returns False
# or: returns True if at least one of the conditions is true, otherwise returns False
# not: returns True if the condition is false, and False if the condition is true
# Example of logical operators
age = 25
is_student = False
# Using and operator
if age >= 18 and not is_student:
    print("You are an adult and not a student.")
# Using or operator
if age >= 18 or is_student:
    print("You are either an adult or a student.")
# Using not operator
if not is_student:
    print("You are not a student.")
    
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("You are eligible for a loan.")
elif has_high_income or has_good_credit:
    print("You might be eligible for a loan.")
else:
    print("You are not eligible for a loan.")
    
#another example of logical operators with relational operators
temperature = 30
is_sunny = True
if temperature > 25 and is_sunny:
    print("It's a great day for a picnic!")
elif temperature > 25 or is_sunny:
    print("It's a nice day, but not perfect for a picnic.")
else:
    print("It's not a good day for a picnic.")
    
    
    #exercise question checking the validity of a name based on its length using logical operators
    
name= "Alice"
name_length = len(name)
if name_length < 3:
    print("Name must be at least 3 characters long.")
elif name_length > 50:
    print("Name must be less than 50 characters long.")
else:
    print("Name is valid.")