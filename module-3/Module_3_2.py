# Noel Miranda, June 18, 2024, Module 3.2 assignment Redo.

# The purpose of this program is to determine how long it 
# takes for an investment to double at a given interest rate 
# while utilizing a while loop. I have also implemented a validation
# for input to continue my practice of the learning. 



def main(): 
    # Displays intro message.
    program_intro()
    # Calling function to retrieve inputs.
    annual_interest_rate = user_input_1()
    initial_investment = user_input_2()
    # This is calling the calculation function. 
    years = program_calculation_for_years(annual_interest_rate, initial_investment) 
    # This will print out the output.
    print('It will take', years, 'years for your investment to double.')

# This is an intro function to introduce the user to the program.
def program_intro():
   print('\nWelcome! ')
   print('\nThis is an investment calculator program in order to help ')
   print('you figure out how long in years it will take for your initial ')
   print('investment to double based of your annualized interest rate.')
   print()

# Retrieving interest rate from user with validation.
def user_input_1():
     while True:
        try:
             # This will retrieve user input.
            annual_interest_rate = float(input('What is your annualized interest ' +
                                            'rate percentage without the percentage symbol?: '))
             # Validation
            if annual_interest_rate <= 0:
                    print('Non-negative inputs only. Try again') 
            else:
                 return annual_interest_rate
        except ValueError:
                print('Only numerical values are accepted. Please try again.')

# Retrieving initial investment from user with validation.
def user_input_2():
     while True:
        try:
             # This will retrieve user input.
            initial_investment = float(input('What is your initial investment?: '))

             # Validation
            if initial_investment <= 0:
                    print('Non-negative inputs only. Try again') 
            else:
                 return initial_investment
        except ValueError:
                print('Only numerical values are accepted. Please try again.')

# This is a function that calculates the ouput based of the input using 
# a while loop. 
def program_calculation_for_years(interest_rate, starting_investment):
   years = 0
   target_goal = 2 * starting_investment
   current_amount = starting_investment

   while current_amount < target_goal:
        current_amount += current_amount * (interest_rate / 100)
        years += 1

   return years


#Executes the main function when on the main program
if __name__ == "__main__":
   main()

#Cited sources for this program
print (f'\n\t\t***{'Bibliography':^20}***')
print ('Gaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')