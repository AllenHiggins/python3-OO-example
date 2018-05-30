from ABC_Employee import Employee
from FullTimeEmployee import FullTimeEmployee

# create new objects
person1 = FullTimeEmployee('Alan', 'Coy', 55000,7)
person1.apply_raise(1.24)

person2 = FullTimeEmployee('Tom', 'Robberts', 55000,7)
person2.apply_raise(1.01)
 
# String formate convert constructor example
person3 = "Sam-Simth-40000-6"
person3 = FullTimeEmployee.from_str_init(person3,'-')

# type of employee - inheritance
person4 = FullTimeEmployee('John', 'Davis', 35000, 5)
person4.level_up()

# Test Outputs
print("Object: {} \nName: {} \nPay: {} \n".format( "person1", person1.full_name(), person1.pay ))
print("Object: {} \nName: {} \nPay: {} \n".format( "person2", person2.full_name(), person2.pay ))
print("Object: {} \nName: {} \nPay: {} \n".format( "person3", person3.full_name(), person3.pay ))
print("Object: {} \nName: {} \nPay: {} \nLevel: {} \n".format( "person4", person4.full_name(), person4.pay, person4.level ))
print(person4.say_hello())
print(person1.do_something())
print("\nTotal Employees: {}".format(Employee.num_of_employees))