#?9. Abstract Classes and Methods
#?Assignment:
#?Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC , abstractmethod


# Import ABC and abstractmethod for abstract class
from abc import ABC, abstractmethod

# Define abstract base class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Test the Rectangle class
rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")  # Output: Area: 15
    

class Shape1(ABC):
  @abstractmethod
  def area(self):
    pass

class Square(Shape1):
  def __init__(self, width, hight):
    self.width = width
    self.hight = hight

  def area(self):
    return self.hight * self.width


square = Square(4,4)
print(square.area())

