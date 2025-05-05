class Engine:
    def start(self):                 # Engine class ka method jo engine ko start karta hai
        return "Engine Started"

class Car:
    def __init__(self, engine):      # Constructor jo Engine object ko accept karta hai
        self.engine = engine         # Engine object ko Instance variable mein store karta hai
    
    def start_car(self):             # Car class ka method jo Engine ke start method ko access karta hai
        return self.engine.start()   # Engine ka start method call karega

# Example usage:
engine = Engine()                    # Engine ka object banaya hai
car = Car(engine)                    # Car ka object banaya aur engine pass kiya hai
print(car.start_car())               # Car ke zariye engine ko start karein gaye