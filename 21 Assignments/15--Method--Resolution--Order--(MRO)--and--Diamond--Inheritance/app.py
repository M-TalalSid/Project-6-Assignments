class A:
    def show(self):                 # Base class A ka method
        print("This Is Class A")

class B(A):                         # Class B jo A se inherit karta hai
    def show(self):                 # Class A ka show method override karta hai
        print("This Is Class B")

class C(A):                         # Class C jo A se inherit karta hai
    def show(self):                 # Class A ka show method override karta hai
        print("This Is Class C")

class D(B, C):                      # Class D jo B aur C dono se inherit karta hai (Diamond Inheritance)
    pass                            # Show method override nahi kiya, MRO ke hisaab se method call hoga

d = D()                             # D ka object banaya hai
d.show()                            # Show method call kiya hai, MRO ke hisaab se result dekhein gaye

# MRO ko dekhne ke liye
print(D.__mro__)                    # D ka Method Resolution Order print karega