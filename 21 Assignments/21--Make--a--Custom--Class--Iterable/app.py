class Countdown:
    def __init__(self, start):    # Constructor jo start number set karta hai
        self.start = start        # Start number ko instance variable mein store karta hai
    
    def __iter__(self):           # __iter__ method jo object ko iterable banata hai
        return self               # Khud ko return karta hai kyun ke yeh iterator bhi hai
    
    def __next__(self):           # __next__ method jo agla number return karta hai
        if self.start < 0:        # Agar start 0 se kam ho gaya
            raise StopIteration   # Loop ko stop karne ke liye exception raise karta hai
        current = self.start      # Current value ko store karta hai
        self.start -= 1           # Start ko ek se kam karta hai
        return current            # Current value return karta hai

countdown = Countdown(10)         # Countdown ka object banaya hai aur start number 10 set kiya hai
for num in countdown:             # For loop mein object ko iterate kiya hai
    print(num)                    # Har number ko print karega