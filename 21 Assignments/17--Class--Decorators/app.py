def add_greeting(cls):                       # Class decorator jo class ko modify karta hai
    class WrappedClass(cls):                 # Inner class jo original class ko wrap karta hai
        def greet(self):                     # Naya method jo class mein add kiya jata hai
            return "Hello From Decorator!"
    
    return WrappedClass                      # Modified class return karta hai

@add_greeting                                # Decorator ko Person class pe apply karta hai
class Person:
    def __init__(self, name):                # Constructor jo name set karta hai
        self.name = name

person = Person("Talal")                     # Person ka object banaya hai
print(person.greet())                        # Yeh naye add kiye gaye "greet" method ko call karega