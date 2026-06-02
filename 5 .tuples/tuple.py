# tuples are imutable, ordered collections of elements that can be of different types. They are defined using parentheses () and can contain any number of elements. Tuples are similar to lists, but they cannot be modified after they are created. This means that you cannot add, remove, or change elements in a tuple once it has been defined.
# Example of a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(my_tuple)
print(type(my_tuple))  # Output: <class 'tuple'>
names = ("Alice", "Bob", "Charlie")
print(names)
print(type(names))  # Output: <class 'tuple'>
# Accessing tuple items
print(names[0])  # Output: Alice
# Tuples are immutable, so you cannot modify them
# names[1] = "Robert"  # This will raise a TypeError
# Tuple methods 
print(names.count("Alice"))  # Output: 1 (counts the occurrences of "Alice" in the tuple)
print(names.index("Charlie"))  # Output: 2 (returns the index of the first

# occurrence of "Charlie" in the tuple)
# Finding the length of a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(len(my_tuple))  # Output: 4

# magic items or methods of tuple
my_tuple = (1, 2, 3)
print(min(my_tuple))  # Output: 1
print(max(my_tuple))  # Output: 3
  
  # we use thse _ _ to access the magic methods of the tuple class for example, we can use __class_getitem__ to get the type of the first element in the tuple, __len__ to get the number of elements in the tuple, and __getitem__ to get the element at a specific index in the tuple. the reaon they are diffrent from the normal methods is that they are called by the python interpreter when we use certain syntax, for example, when we use square brackets to access an element in a tuple, the __getitem__ method is called automatically by the interpreter.
  #benfits of using magic methods is that they allow us to define custom behavior for our classes when we use certain syntax, for example, we can define a __str__ method to return a string representation of our class when we print it, or we can define a __add__ method to allow us to add two instances of our class together using the + operator. Magic methods are a powerful tool for creating classes that behave in a way that is intuitive and easy to use.
my_tuple.__class_getitem__(0)  # Output: <class 'int'> (returns the type of the first element in the tuple)
my_tuple.__len__()  # Output: 3 (returns the number of elements in the tuple)
my_tuple.__getitem__(1)  # Output: 2 (returns the element at index 1 in the tuple) 
