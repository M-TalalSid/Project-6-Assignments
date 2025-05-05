def log_function_call(func):                # Decorator function jo function call ko log karta hai
    def wrapper():                          # Inner function jo Decorated function ko wrap karta hai
        print("Function is being called")   # Function call hone se pehle message print karta hai
        func()                              # Original function ko call karta hai
    return wrapper                          # Wrapper function return karta hai

@log_function_call                          # Decorator ko say_hello function pe apply karega
def say_hello():                            # Function jo "Hello World" print karta hai
    print("Hello World !")

say_hello()                                 # Decorator wala function call kiya hai