class Employee:
    def __init__(self, name):                                                  # Employee class ka constructor jo name set karta hai
        self.name = name                                                       # Name ko instance variable mein store karta hai
    
    def get_details(self):                                                     # Method jo employee ka name return karega
        return f"Employee: {self.name}"

class Department:
    def __init__(self, dept_name, employee):                                   # Constructor jo Department ka Name aur Employee ka Reference leta hai
        self.dept_name = dept_name                                             # Department ka name set karega
        self.employee = employee                                               # Employee object ka Reference store karta hai (aggregation)
    
    def get_details(self):                                                     # Method jo department aur employee ki details dikhaye ga
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

emp = Employee("Faraz")                                                        # Employee ka object banaya hai
dept = Department("HR", emp)                                                   # Department ka object banaya aur Employee ka Reference pass kiya hai
print(dept.get_details())                                                      # Department ki details print ki hain