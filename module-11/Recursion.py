# Noel Miranda, July 25, 2024, Module 11.2 assignment.

# The purpose of this program is to familiarize oneself with recursive functions. 
# This program will create a recursive function that accepts an integer
# argument, n, and prints the number of 1 and up to and including n. For
# comparison purposes, there will be a non-recursive method for the same functionality.

# Main function.
def main():
    
    # Descriptive intro to the program.
    intro()

    # Assigns returned value from function to n.
    n = prompting_for_n()

    # Asthetic output design to organize information.
    print('------------------------------------------------------------------------')

    # Tells the user which function is being invoked before execution.
    print(f'\nThrough a recursive method and the input of {n}, the \n'
          'following sequence is produced:\n')

    # Recursive function with one paramater. n for desired integer.
    recursive_approach(n)

    # Tells the user which function is was invoked after execution.
    print('\n\nThe recursive method was successful.\n\n')

    # Asthetic output design to organize information.
    print('------------------------------------------------------------------------')

    # Non-recursive function with one paramater. n for desired integer.
    non_recursive_approach(n)

    # Asthetic output design to organize information.
    print('------------------------------------------------------------------------')

    # References function for this program
    references()

    # Asthetic output design to organize information.
    print('========================================================================')

# Descriptive intro to the program.
def intro():
    print('\n\n')
    print('Welcome! This program was built to count from 1 to any number you \n' 
          'desire by a step of 1. This will be achieved through two methods. \n'
          'The first method will be through a recursive approach and the second \n'
          'method will be through a non-recursice approach, in other words an \n'
          'iterative approach. Enjoy!')
    
    # Asthetic output design to organize information.
    print('========================================================================')
    print()

# Function that prompts user for n interger and includes test code that will not
# allow negative or 0 value or non-integer input.
def prompting_for_n():
    while True: 
        try:
            n = int(input('What positive number above zero would you like both of \n'
                          'these approaches to count up to? '))
            if n < 1:
                print('\nInvalid input. Please try again.\n')
            else:
                return n
        except ValueError:
            print('\nInvalid input. Your response must be a number. Please try again.\n')

# In this function the problem is solved by the function calling itself with n-1 until
# it reaches 1. Then, it prints the numbers during the unwind phase of recursion.
def recursive_approach(n):
    if n == 1: 
        print(1, end= ' ')
    else:
        recursive_approach(n-1)
        print(n, end= ' ')

# In this function the problem is solved by a simple while loop that iterates from 
# 1 to n. 
def non_recursive_approach(n):

    # Tells the user which function is being invoked before execution.
    print(f'\nThrough a non-recursive method and the input of {n}, the \n'
          'following sequence is produced:\n')
    
    # accumalator initialized with the value 0.
    a = 0

    # while loop that prints until a equals n.
    while a != n:
        a += 1
        print (a, end=' ')

    # Tells the user which function is was invoked after execution.
    print('\n\nThe non-recursive method was successful. \n\n')

# This is a function to list the cited reference for this program.
def references():
    print (f'\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

# Executes main() function when on main
if __name__ == '__main__':
    main()