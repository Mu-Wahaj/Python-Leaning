## return statement in python  is used to exit a function and return a value to the caller. It can be used to return any type of data, including numbers, strings, lists, dictionaries, or even other functions. When a return statement is executed, the function terminates immediately and the specified value is sent back to the caller.
# Example of a function with a return statement
def square(x):
    return x * x
result = square(5)
print(result)  # Output: 25
# Function that returns a string
def greet(name):
    return f"Hello, {name}!" ##f-string is a way to format strings in python. It allows you to embed expressions inside string literals, using curly braces {} unlike C++ where we use %. The expressions are evaluated at runtime and their values are inserted into the string at the corresponding positions.
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Another example of a function that returns a list
def get_numbers():
    return [1, 2, 3, 4, 5]
numbers = get_numbers()
print(numbers)  # Output: [1, 2, 3, 4, 5]


## reorganizing the emoji function in dictionaries/practice.py using return statement

## what this do is it takes a message as input, splits it into words, and then checks if each word is an emoji code defined in the emojis dictionary. If it finds a match, it replaces the word with the corresponding emoji. Finally, it returns the converted message as a string.    
def convert_to_emoji(message):
    words = message.split(" ")  
    emojis = { ## a dictionary that maps emoji codes to their corresponding emojis
        ":)": "😊",
        ":(": "😢",
        "3>": "❤️",
        "(:": "😠",
    }
    converted_message = ""
    for word in words:
        if word in emojis:
            converted_message += emojis[word] + " " ## if the word is found in the emojis dictionary, it appends the corresponding emoji to the converted_message string, followed by a space for separation. If the word is not found in the emojis dictionary, it appends the original word to the converted_message string, followed by a space for separation. Finally, it returns the converted_message string with any trailing space removed using the strip() method.
        else:
            converted_message += word + " "
    return converted_message.strip()  # Remove trailing space

message = input("Enter a message: ")
converted_message = convert_to_emoji(message)
print(converted_message)