#dictionaories in python  are unordered collections of key-value pairs. They are defined using curly braces {} and each key is separated from its value by a colon :. Dictionaries are mutable, which means that you can change their content after they have been created. You can add, remove, or modify key-value pairs in a dictionary.
# Example of a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
print(type(my_dict))  # Output: <class 'dict'>
# Accessing dictionary items
print(my_dict["name"])  # Output: Alice
# Modifying dictionary items
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# Adding new key-value pairs to the dictionary
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
# Removing key-value pairs from the dictionary
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}


# Dictionary methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country']) (returns a view object containing the keys of the dictionary)
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'USA']) (returns a view object containing the values of the dictionary)
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')]) (returns a view object containing the key-value pairs of the dictionary as tuples) it returns a dictionary as tuples where each tuple contains a key and its corresponding value from the dictionary. This allows us to easily iterate over the key-value pairs in the dictionary using a for loop or other iterable methods.

#more dictionary methods
print(my_dict.get("name"))  # Output: Alice (returns the value associated with the key "name", or None if the key is not found)
print(my_dict.get("gender", "Not specified"))  # Output: Not specified (returns the value associated with the key "gender", or "Not specified" if the key is not found)
print(my_dict.pop("age"))  # Output: 31 (removes the key "age" from the dictionary and returns its value) it removes last key-value pair from the dictionary and returns the value of the removed key. If the dictionary is empty, it raises a KeyError.
print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA         
print(my_dict.popitem())  # Output: ('country', 'USA') (removes and returns an arbitrary key-value pair from the dictionary as a tuple)
print(my_dict)  # Output: {'name': 'Alice'} (the remaining key-value pair in the dictionary after popitem() is called)

