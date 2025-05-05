class Logger:
    def __init__(self):                     # Constructor jo object Banne par message print karega
        print("Logger Object Created.")

    def __del__(self):                      # Destructor jo object Destroy hone par message print karega
        print("Logger Object Destroyed.")

# Ek object banaya hai
logger = Logger()

# Ye Object ko delete karne ke liye
del logger