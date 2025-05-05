from abc import ABC, abstractmethod

class Shape(ABC):                           # Abstract base class Shape (Yeh ek abstract base class hai jiska name "Shape" hai aur yeh ABC se inherit karta hai)
    @abstractmethod
    def area(self):                         # Abstract method jo subclasses mein implement hona chahiye
        pass

class Rectangle(Shape):                     # Rectangle class jo Shape se inherit karta hai
    def __init__(self, length, width):      # Constructor Length aur Width ko set karta hai
        self.length = length
        self.width = width
    
    def area(self):                         # Abstract method area ko implement karta hai
        return self.length * self.width     # Rectangle ka area length * width hai

# Example usage:
rect = Rectangle(9, 3)                      # Rectangle ka object banaya hai
print(f"Rectangle Area: {rect.area()}")     # Area Calculate aur Print kiya hai