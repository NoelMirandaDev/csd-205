# Noel Miranda, July 5, 2024, Module 7.2 assignment.

# The purpose of this program is to familiarize oneself further with strings.
# This program will acquire a full name input, as a string, and 
# display that full name in initials format. 

def main():
    intro()

    # Request full name from user.
    first_name = input('First name: ')
    middle_name = input('Middle name (If no middle name leave blank): ')
    last_name = input('Last name: ')
    print()

    # Converts full name to initials format and displays it back to user.
    print(f' Your full name in initials format is {initials_Format(first_name,middle_name,last_name)}')
    print()

    # Imported references function for references of this code.
    references()

# Introduction to program. 
def intro():
    print()
    print('Welcome user! This is a program which retrieves '
          '\nyour full name and displays it in initals format.')
    print()
    
# Converts full name to initials format.
def initials_Format(first_name,middle_name,last_name):
    f_initial = f'{first_name[0]}.'
    
    # if/else block for scenarios where user does not have middle name
    if middle_name:
        m_initial = f'{middle_name[0]}.'
    else:
        m_initial = ''

    l_initial = f'{last_name[0]}.'

    # Concatenate full name initials together.
    full_name_initials = f_initial + m_initial + l_initial

    return full_name_initials

# This is a function to list the cited reference for this program.
def references():
    print (f'\n\n\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

if __name__ == '__main__':
    main()




