# classes in pyhton are blueprints for creating objects. They encapsulate data and functions that operate on that data. Here's a simple example of a class in Python:
class Person:
    def move(self):
        print("The person is moving.")
    
    def eat(self):
        print("The person is eating.")
        
        
# Creating an instance of the Person class
person1 = Person()
# Calling methods on the instance
person1.move()  # Output: The person is moving.
person1.eat()   # Output: The person is eating.
# Another example of a class with attributes and methods
class Car:
    def  model(self, model_name):
        self.model_name = model_name  # This is an attribute of the Car class
    def start_engine(self):
        print(f"The {self.model_name} engine is starting.")
# Creating an instance of the Car class
car1 = Car()
car1.model("Toyota")  # Setting the model attribute
car1.start_engine()  # Output: The Toyota engine is starting.
