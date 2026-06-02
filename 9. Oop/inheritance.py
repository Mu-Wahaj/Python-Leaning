# inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes. In Python, inheritance is implemented by defining a new class that specifies the parent class in parentheses. Here's an example of inheritance in Python:

class Mammal:
    def walk(self):
        print("walking.")


class Dog(Mammal):
    def bark(self):
        print("barking.")
        
class Cat(Dog):
    def meow(self):
        print("meowing.")
# Creating instances of the Dog and Cat classes
dog1 = Dog()        
cat1 = Cat()
# Calling methods from the Dog class
dog1.walk()  # Output: walking.
dog1.bark()  # Output: barking.
# Calling methods from the Cat class
cat1.walk()  # Output: walking.
cat1.bark()  # Output: barking. (inherited from Dog class)
cat1.meow()  # Output: meowing. (defined in Cat class)

# note one s cat is inheriting from dog and dog is inheriting from mammal so cat can access the methods of both dog and mammal class.