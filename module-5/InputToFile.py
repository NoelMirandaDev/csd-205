# Noel Miranda, June 22, 2024, Module 5.2 assignment.

# The purpose of this program is to prompt a user to input
# a file name, their name, their street address, and 
# their phone number. Everything, except the file name, will be written
# to a comma-seperated line in a file named by the user. Then, 
# the program will read that data of the file and display its contents.



def main():
    program_intro()

    # Retrieves data input about the user. 
    file_name = input('How would you like to name the file where you want your ' 
          'information saved to? ')
    user_name = input('What is your name? ')
    user_address = input('What is your current address? ')
    user_phone_number = input('What is your phone number? ')

    outfile(file_name, user_name, user_address, user_phone_number)
    infile(file_name)
    sources()

# This is an intro function to introduce the user to the program.
def program_intro():
    print('\nWelcome! ')
    print('\nThis is a program requiring your input on three fields about yourself. \n'
          'The objective is to save that data as a record on a new file named as '
          'you desire, \nand then read that file to display your updated record.')
    print()

# This is a function to create a file as the user named to write the data into.
def outfile(file_name, user_name, user_address, user_phone_number):
    # Opens file named by user.
    outfile = open(f'{file_name}.txt', 'w')

    # Writes the input data to a comma-seperated line in the outfile.
    outfile.write(user_name + ', ' + user_address + ', ' + user_phone_number + '. \n')

    # Closes file. 
    outfile.close()
    print('Data Successfully saved to file.')
    print()

# This is a function to read the data from the file and display its contents.
def infile(file_name):

    print('Retrieving contents of file now... ')
    print()

    # Opens file named by user.
    infile = open(f'{file_name}.txt', 'r')

    # Reads the contents of the file.
    contents = infile.readline()

    # Strips the newline character.
    contents = contents.strip('\n')

    # Prints the contents of file.
    print(contents)

    # Closes file. 
    infile.close()

# This is a function to list the cited sources for this program.
def sources():
    print (f'\n\n\n***{'Sources':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

#Executes the main function when on the main program
if __name__ == "__main__":
   main()