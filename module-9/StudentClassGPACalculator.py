# Noel Miranda, July 13, 2024, Module 9.2 assignment.

# The purpose of this program is to familiarize oneself with the class
# object. This program will create an object called student which 
# will then create an instance of the student class to calculate
# the a student's GPA depending on the user's inputs.  

class Student:

    # The __init__ method initializes the data attributes.
    def __init__(self,first_name,last_name): 
        self.__fname = first_name
        self.__lname = last_name

    # The set_fname method accepts an argument for the student's
    # first name.      
    def set_fname(self, first_name):
        self.__fname = first_name

    # The set_lname method accepts an argument for the student's
    # last name.
    def set_lname(self,last_name): 
        self.__lname = last_name

    # The get_fname method returns the student's first name
    def get_fname(self):
        return self.__fname
    
    # The get_lname method returns the student's last name
    def get_lname(self):
        return self.__lname
    
    # The retrieve_gpa method calculates the student's gpa based on user's 
    # input of credits and letter grades for the courses taken.
    def retrieve_gpa(self):

        #initialized accumalators
        total_credits = 0
        total_gradepoints = 0
        sum = 0

        # Requires input from user regarding number of courses
        courses = int(input(f'How many courses did {self.__fname}'
                            ' ' f'{self.__lname} take this semester? '))
        print()
        print('Input the credits and grade for each course.')
        print('--------------------------------------------')

        # Loop prompting the user for the credits & grade for each course the student
        # has taken.
        for n in range(1, courses+1):
            credit = int(input(f'The credits for course {n}: '))
            __grade = input(f'The letter grade for course {n}: ')

            if __grade.upper() == 'A':
                __grade = int(4)
            elif __grade.upper() == 'B':
                __grade = int(3)
            elif __grade.upper() == 'C':
                __grade = int(2)
            elif __grade.upper() == 'D':
                __grade = int(1)
            elif __grade.upper() == 'F':
                __grade = int(0)
            else:
                print('Invalid grade entered. Default grade assigned to F.' )
                __grade = int(0)

            # Accumalators
            total_credits += credit
            total_gradepoints += __grade
            sum += __grade * credit
        
        # GPA calculations
        self.__gpa = (sum/total_credits)
    
    # The get_gpa method displays the student's GPA
    def get_gpa(self):
        return print(f"{self.__fname} {self.__lname}'s GPA is {self.__gpa}.")
        
# The main function
def main():

    print()

    # Intro function
    intro()

    print()

    # Prompts user for student's full name
    first_name = input("What is the student's first name? ")
    last_name = input("What is the student's last name? ")

    # Creating an instance of the Student class = object
    student1 = Student(first_name, last_name)

    # Calculates GPA through object's retrieve_gpa method
    student1.retrieve_gpa()

    print()

    # Displays calculated GPA through object's retrieve_gpa method
    student1.get_gpa()

    # Imported references function
    references()

# Intro to program
def intro():
    print('Hello teacher, this program is a GPA calculator for your students.')

# This is a function to list the cited reference for this program.
def references():
    print (f'\n\n\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

# Executes the main function when on the main program
if __name__ == '__main__':
    main()