class InvalidAgeError(Exception):                          # Custom exception class jo Exception se inherit karta hai
    pass                                                   # Sirf ek placeholder, koi extra functionality nahi hai

def check_age(age):                                        # Function jo age check karrga
    if age < 18:                                           # Agar age 18 se kam hai
        raise InvalidAgeError("Age Must Be 18 Or Older")   # Custom exception raise karta hai
    return "Age Is Valid"                                  # Agar age valid hai toh message return karega

# Example usage with try-except
try:
    print(check_age(16))                                   # 16 ke sath function call kiya hai
except InvalidAgeError as e:
    print(f"Error: {e}")                                   # Exception handle kiya aur message print kiya

try:
    print(check_age(25))                                   # 25 Age ke sath function call kiya hai
except InvalidAgeError as e:
    print(f"Error: {e}")                                   # Agar exception aaye gi toh handle karega yeh