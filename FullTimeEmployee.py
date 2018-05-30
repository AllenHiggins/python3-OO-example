from ABC_Employee import Employee

# Inherits from Employee class - also known as a subclass
class FullTimeEmployee(Employee):
    
    # Constructor
    def __init__(self,first_name,last_name,pay,level):
        super().__init__(first_name,last_name,pay)
        self.level = level

    def level_up(self):
        self.level += 1
    
    # class wapper method - cls stands for the class instance as class is a python keyword
    # Constructor for converting from string example
    @classmethod
    def from_str_init(cls, employee_str, split_on_char):
        first_name, last_name, pay, level = map(str, employee_str.split(split_on_char))   
        new_employee = cls(first_name,last_name,pay,level)
        return new_employee 

    # Polymorphism - Overwriting say_hello method in supper class (Employee)
    def say_hello(self):
        return "Hello Galaxy!"

    # Must inherit abstract methods
    def do_something(self):
        return "Hello World!"