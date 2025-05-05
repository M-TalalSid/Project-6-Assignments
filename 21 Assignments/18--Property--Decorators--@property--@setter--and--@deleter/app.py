class Product:
    def __init__(self):                         # Constructor jo private attribute initialize karta hai
        self.__price = 0                        # Private attribute __price ko 0 se initialize kiya hai
    
    @property                                   # Property decorator jo price ko get karne ke liye method banata hai
    def price(self):                            # Getter method jo private price ko return karta hai
        return self.__price
    
    @price.setter                               # Setter decorator jo price ko update karne ke liye method banata hai
    def price(self, value):                     # Setter method jo price ko set karta hai
        if value >= 0:                          # Agar value zero ya zyada hai toh set karlein (Your Choice)
            self.__price = value
        else:
            print("Price Cannot Be Negative")
    
    @price.deleter                              # Deleter decorator jo price ko delete karne ke liye method banata hai
    def price(self):                            # Deleter method jo price ko delete karta hai
        del self.__price
        print("Price Has Been Deleted")

product = Product()                             # Product ka object banaya hai
print(product.price)                            # Yeh getter ke zariye price (0) ko print karega

product.price = 80000000                        # Price ko update kiya hai
print(product.price)                            # New price check karega

del product.price                               # Price ko delete kiya hai
# print(product.price)                          # Yeh error dega kyunki price delete ho chuka hai