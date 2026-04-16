#if statement in python are used to make decisions based on conditions. The basic syntax of an if statement is as follows:
# if condition:
#     # code to execute if the condition is true
# else:
#     # code to execute if the condition is false
# Example of if statement
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Example of if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    #another example of if statement
is_raining = True
if is_raining:
    print("Don't forget to take an umbrella!")
else:
    print("Enjoy the sunny weather!")  
print("This will always be printed regardless of the weather because indentation is important in python .")  
 
 
 #exercise question to calculate down payment based on credit score
house_price = 250000
good_credit = True
if good_credit:
    down_payment = house_price * 0.1
else:   
    down_payment = house_price * 0.2
print(f"Down payment: ${down_payment}")



