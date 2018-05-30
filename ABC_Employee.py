from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    
    num_of_employees = 0
        
    # Constructor
    def __init__(self, first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_employees += 1    
     
    # Methods:
    # self gets passed in automatically so we need to account for it as an argument in the method
    # Property gets current names
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self, amount):
        self.pay = int(self.pay * amount)
    
    # We will so how Polymorphism works with this method in subclasses
    def say_hello(self):
        return "Hello World!"
    
    # Must create at least one abstract signature in order to implment an Absrtact class
    @abstractmethod
    def do_something(self):
        raise NotImplementedError
