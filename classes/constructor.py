# constructor like many  progarraming languages is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method. Here's an example of a class with a constructor in Python:

class Point:
    def __init__(self, x, y):
        self.x = x  # This is an attribute of the Point class
        self.y = y  # This is another attribute of the Point class
        print(f"Point created at ({self.x}, {self.y})")  # This will print a message when a Point object is created
    def move(self):
        print(f"The point is moving to ({self.x}, {self.y}).")
# Creating an instance of the Point class
point1 = Point(2, 3)
point1.x = 11
point1.move()  # Output: The point is moving to (11, 3).


class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, {self.age} years old.")
    def talk(self):
        print(f"{self.name} is talking.")
    
person1 = person("Alice", 30)
person1.talk()  # Output: Alice is talking.

# detsucturor is a special method that is automatically called when an object of a class is destroyed. It is used to perform any cleanup actions that may be necessary when an object is no longer needed. In Python, the destructor method is defined using the __del__() method. Here's an example of a class with a destructor in Python:
class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"MyClass object created with value: {self.value}")
    def __del__(self):
        print(f"MyClass object with value {self.value} is being destroyed.")
obj = MyClass(10)
del obj  # This will trigger the destructor and print the message. its is nescory to note that the destructor may not be called immediately when an object is deleted, as it depends on the garbage collection process of Python.del  is not nsecary to call the destructor, it is automatically called when the object is garbage collected.