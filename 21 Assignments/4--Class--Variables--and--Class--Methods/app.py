class Bank:
    bank_name = "State Bank"                                           # Class variable jo tamaam Instances ke liye bank ka name rakhega

    def __init__(self, branch):
        self.branch = branch                                           # Har Instance ke liye alag branch

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name                                           # Class method jo bank ka name change karega aur yeh tamaam Instances ko affect karega

    def display(self):
        print(f"Bank Name: {self.bank_name}, Branch: {self.branch}")   # Method jo bank ka name aur branch dikhaye ga

# Instances banaye hain
bank1 = Bank("Karachi")
bank2 = Bank("Islamabad")

# Pehle bank ka name aur branch check karein gaye
print("Before Changing Bank Name:")
bank1.display()
bank2.display()

# Bank ka name change karein gaye
Bank.change_bank_name("National Bank")

# Baad mein bank ka name aur branch check karein gaye
print("\nAfter Changing Bank Name:")
bank1.display()
bank2.display()