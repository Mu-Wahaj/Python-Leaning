# Arithemtc operations in python
# Addition
a = 10
b = 5
addition = a + b
print("Addition:", addition)
# Subtraction
subtraction = a - b
print("Subtraction:", subtraction)
# Multiplication
multiplication = a * b
print("Multiplication:", multiplication)
# Division
division = a / b
print("Division:", division)
# Floor Division
floor_division = a // b
print("Floor Division:", floor_division)
# Modulus
modulus = a % b
print("Modulus:", modulus)
# Exponentiation
exponentiation = a ** b ## a raised to the power of b > a^b>10^5
print("Exponentiation:", exponentiation)

# increment and decrement
a += 1  # Increment a by 1
print("Incremented a:", a)
b -= 1  # Decrement b by 1
print("Decremented b:", b)
# it does not change the original value of a and b, it returns a new value and assign it to a and b respectively    
print("a + b =", a + b)
# opertaor precedence
result = a + b * 2  # Multiplication has higher precedence than addition
print("Result of a + b * 2:", result)
# using parentheses to change precedence    
result_with_parentheses = (a + b) * 2  # Parentheses change the order of operations
print("Result of (a + b) * 2:", result_with_parentheses)

# exponents 
# multiplications and divisions are evaluated before additions and subtractions
result_exponents = a + b * 2 ** 3  # Exponentiation has higher precedence than multiplication and addition
print("Result of a + b * 2 ** 3:", result_exponents)
