class Dog:
    def __init__(self, name, breed):       # Constructor jo Name aur Breed ko Initialize karta hai
        self.name = name                   # Instance variable name ko set karega 
        self.breed = breed                 # Instance variable Dog ki breed ko set karega
    
    def bark(self):                        # Instance method jo dog ke bark ka message print karega
        print(f"{self.name} Is Barking!")  # Dog ka name include karke message print karega

# Example usage:
my_dog = Dog("Leo", "Siberian Husky")      # Dog ka object banaya hai
my_dog.bark()                              # Bark method ko call kiya hai