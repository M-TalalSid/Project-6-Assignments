class Person:
    def __init__(self, name):            # Person class ka Constructor jo name set karega
        self.name = name                 # Name ko Instance variable mein store karta hai

class Teacher(Person):
    def __init__(self, name, subject):   # Teacher class ka Constructor
        super().__init__(name)           # super() se Person class ka Constructor call kiya jaye ga
        self.subject = subject           # Subject ko Instance variable mein store karta hai
    
    def display(self):                   # Method jo Teacher ki details dikhaye ga
        print(f"Name: {self.name}, Subject: {self.subject}")

teacher = Teacher("Ali", "Mathematics")  # Teacher ka object banaya hai
teacher.display()                        # Display method ko call hai