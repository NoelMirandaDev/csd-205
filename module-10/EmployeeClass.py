# Noel Miranda, July 20, 2024, Module 10.2 assignment.

# The purpose of this program is to familiarize oneself with class
# objects, specifically working with superclass, subclass, and polymorphism. 
# This program will create a class called Employee and a subclass of Employee
# called an instance of ProductionWorker. This program will display the output
# to the user. 

# Employee class initialized
class Employee: 
    # Employee class data attributes
    def __init__(self, emp_name, emp_gender, emp_hpr, emp_num):
        self.__emp_name = emp_name
        self.__emp_gender = emp_gender
        self.__emp_hpr = emp_hpr
        self.__emp_num = emp_num

    # Mutator method
    def set_emp_name(self,emp_name):
        self.__emp_name = emp_name

    # Mutator method
    def set_emp_gender(self, emp_gender):
        self.__emp_gender = emp_gender

    # Mutator method
    def set_emp_hpr(self, emp_hpr):
        self.__emp_hpr = emp_hpr

    # Mutator method
    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num

    # Accessor method
    def get_emp_name(self):
        return self.__emp_name
    
    # Accessor method
    def get_emp_gender(self):
        return self.__emp_gender
    
    # Accessor method
    def get_emp_hpr(self):
        return self.__emp_hpr
    
    # Accessor method
    def get_emp_num(self):
        return self.__emp_num

# ProductionWorker subclass for Employee Superclass  
class ProductionWorker(Employee):
    # Initiliazed data attributes for subclass
    def __init__(self, emp_name, emp_gender, emp_hpr, emp_num, emp_shift_num):
        # Superclass's __init__ method called with required attributes
        Employee.__init__(self, emp_name, emp_gender, emp_hpr, emp_num)
        # Initialize data attribute specific to subclass
        self.__emp_shift_num = emp_shift_num

    # Method as mutator for data attribute
    def set_emp_shift_num(self, emp_shift_num):
        self.__emp_shift_num = emp_shift_num

    # Method as accessor for data attribute
    def get_emp_shift_num(self):
        return self.__emp_shift_num
    
# Main Function    
def main():
    #Descriptive intro to program
    intro()
    
    # Initialized two instances for the Employee class and two for the ProductionWorker class.
    # "x" inputs for all attributes due to requirements of project asking to input the data
    # attributes using the setter methods.
    employee1 = Employee('x','x','x','x')
    employee2 = Employee('x','x','x','x')
    employee3 = ProductionWorker('x','x','x','x','x')
    employee4 = ProductionWorker('x','x','x','x','x')

    # Setting data attributes for employee1 object
    employee1.set_emp_name('Jake Paul')
    employee1.set_emp_gender('Male')
    employee1.set_emp_hpr(20.00)
    employee1.set_emp_num(1111)

    # Setting data attributes for employee2 object
    employee2.set_emp_name('Jennifer Lawrence')
    employee2.set_emp_gender('Female')
    employee2.set_emp_hpr(100.00)
    employee2.set_emp_num(2222)

    # Setting data attributes for employee3 object
    employee3.set_emp_name('Tom Hanks')
    employee3.set_emp_gender('Male')
    employee3.set_emp_hpr(150.00)
    employee3.set_emp_num(3333)
    employee3.set_emp_shift_num('(1) Day Shift')

    # Setting data attributes for employee4 object
    employee4.set_emp_name('Will Ferrell')
    employee4.set_emp_gender('Male')
    employee4.set_emp_hpr(250.00)
    employee4.set_emp_num(4444)
    employee4.set_emp_shift_num('(2) Swing Shift')

    # Getting and displaying data attributes for employee1 object
    print('Name:',f'{employee1.get_emp_name()}')
    print('Gender:',f'{employee1.get_emp_gender()}')
    print('Hourly Pay Rate:','$'f'{employee1.get_emp_hpr():,.2f}')
    print('Employee Number:',f'{employee1.get_emp_num()}')
    print()

    # Getting and displaying data attributes for employee2 object
    print('Name:',f'{employee2.get_emp_name()}')
    print('Gender:',f'{employee2.get_emp_gender()}')
    print('Hourly Pay Rate:','$'f'{employee2.get_emp_hpr():,.2f}')
    print('Employee Number:',f'{employee2.get_emp_num()}')
    print()

    # Getting and displaying data attributes for employee3 object
    print('Name:',f'{employee3.get_emp_name()}')
    print('Gender:',f'{employee3.get_emp_gender()}')
    print('Hourly Pay Rate:','$'f'{employee3.get_emp_hpr():,.2f}')
    print('Employee Number:',f'{employee3.get_emp_num()}')
    print('Employee Shift Number:',f'{employee3.get_emp_shift_num()}')
    print()

    # Getting and displaying data attributes for employee4 object
    print('Name:',f'{employee4.get_emp_name()}')
    print('Gender:',f'{employee4.get_emp_gender()}')
    print('Hourly Pay Rate:','$'f'{employee4.get_emp_hpr():,.2f}')
    print('Employee Number:',f'{employee4.get_emp_num()}')
    print('Employee Shift Number:',f'{employee4.get_emp_shift_num()}')
    print()

    # Refences function.
    references()

# Intro function
def intro():
    print()
    print('Welcome Manager. This program was built to display ')
    print('your workforce team and their information.')
    print('-----------------------------------------------------')
    print()

# This is a function to list the cited reference for this program.
def references():
    print (f'\n\n\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

# Executes main() function when on main
if __name__ == '__main__':
    main()