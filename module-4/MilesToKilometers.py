# Noel Miranda, June 18, 2024, Module 4.2 assignment.

# The purpose of this program is to creat a function that converts
# miles to kilometers. It includes validation of user input with 
# try/except blocks.

#Global Constant of conversion from miles to kilometers
MI_TO_KM_CONVERSION_RATE = 1.60934

def main():
   #displays intro message.
   program_intro()
   #returns input for miles and assigns to local variable.
   miles_to_be_converted = miles_input()
   #passes user input as argument to conversion.
   kilometers_output = mi_to_km_conversion (miles_to_be_converted)
   #displays the values of miles and kilometers from the input.
   display_outputs(miles_to_be_converted,kilometers_output)



#This is an intro function to introduce the user to the program.
def program_intro():
   print('\nWelcome! ')
   print('\nThis is a miles to kilometers conversion calculator.')
   print()

#This is a function to receive the number of miles to be converted.
#Also includes validation of user input for inputs less than zero. 
#Also includes try/except block for invalid input of ValueError.
def miles_input():
   while True:
      try:
        miles = float(input('How many miles have you driven? '))
        if miles < 0: 
            print('\nMiles input cannot be less than zero. Try again.')
        else:   
            return miles
      except ValueError:
         print('Invalid input. Please enter a number.')

#This is a function doing the conversion from miles to kilometers. 
def mi_to_km_conversion(miles):
   kilometers = miles * MI_TO_KM_CONVERSION_RATE
   return kilometers

#This function displays the values of miles and kilometers from the input.
def display_outputs(miles,kilometers):
   print(f'\nThe driven miles that were converted was {miles} miles and the')
   print(f'resulting conversion in kilometers is {kilometers} kilometers.')

#Executes the main function.
main()

#Cited sources for this program
print (f'\n\t\t***{'Bibliography':^20}***')
print ('Gaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
