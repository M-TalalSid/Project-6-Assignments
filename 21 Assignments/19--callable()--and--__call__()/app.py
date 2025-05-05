class Multiplier:
    def __init__(self, factor):      # Constructor jo factor ko set karta hai
        self.factor = factor         # Factor ko instance variable mein store karta hai
    
    def __call__(self, value):       # __call__ method jo object ko function ki tarah call karne ke liye hai
        return self.factor * value   # Input value ko factor se multiply karega

multiplier = Multiplier(100)         # Multiplier ka object banaya hai aur factor ko 100 set kiya hai
print(multiplier(100))               # Object ko function ki tarah call kiya hai (100 * 100)

# Test karne ke liye callable() function use kiya
print(callable(multiplier))          # Check karta hai ke object callable hai ya nahi