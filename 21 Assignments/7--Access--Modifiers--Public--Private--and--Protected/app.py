class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name                        # Public variable jo har jagah access ho sakta hai
        self._salary = salary                   # Protected variable jo Class aur Subclass mein access ho sakta hai
        self.__ssn = ssn                        # Private variable jo sirf class ke andar access ho sakta hai

# Object banaya
emp = Employee("Talal", 95000, "333-22-4444")

# Public variable ko access karna
print("Name:", emp.name)                        # Yeh kaam karega kyun ke name Public hota hai

# Protected variable ko access karna
print("Salary:", emp._salary)                   # Yeh kaam karega lekin recommended nahi kyun ke salary Protected hai

# Private variable ko access karne ki koshish karna
try:
    print("SSN:", emp.__ssn)                    # Yeh error dega kyun ke __ssn Private hai
except AttributeError as e:
    print("Error:", e)                          # Yeh Error message print karega