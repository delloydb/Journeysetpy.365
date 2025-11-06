# learning how to create and use classes in python
# A class is a blueprint for creating objects. It defines a set of attributes and methods that
# the created objects will have.
# An object is an instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name  # constructor
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# Call methods on the my_dog object
my_dog.sit()
my_dog.roll_over()
