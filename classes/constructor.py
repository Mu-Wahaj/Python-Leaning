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