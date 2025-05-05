class Car:
    def __init__(self, brand):                     # Constructor jo car ka brand set karta hai
        self.brand = brand                         # Public variable brand ko initialize karne k liye

    def start(self):                               # Public method start jo car ko start karega
        print(f"{self.brand} Car Has Started.")    # Car ka brand print karega aur start ka message dega

# Class ka ek instance banaya
my_car = Car("BMW")                                # Car class ka object banaya aur brand "BMW" rakha hai mai ne 

# Public variable aur method ko bahar se access karne k liye
print(my_car.brand)                                # Car ka brand print karega
my_car.start()                                     # Car ko start method ke zariye start karega