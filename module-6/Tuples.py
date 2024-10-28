# Noel Miranda, June 28, 2024, Module 6.2 assignment.

# The purpose of this program is to familiarize oneself with the tuple
# function. This program will have a tuple initialized with 20
# related values, specficially automobile brands, and there will be code 
# displaying those values, iterating through each value to display an
# output that has the value in a sentence, and reverse it in the end. 

def main():
    # Tuple initialized with 20 automobile brand values.
    automobiles_tuple = ('Volvo','Volkswagen','Toyota','Ford',
                         'BMW','Kia','Audi','Mercedes-Benz',
                         'Nissan','Hyundai','Mazda','Chevrolet',
                         'Subaru','Tesla','Honda','Fiat','Mitsubishi',
                         'Porsche','Mini','Jeep')
    
    print()
    print(automobiles_tuple) #Displays the contents in a single statement.
    print()
    tuple_iterated(automobiles_tuple) #Iterates through each element.
    print()
    tuple_iterated_reversed(automobiles_tuple) #One way to repeat the output in reverse order.
    print()
    tuple_iterated_reversed_2(automobiles_tuple) #Second way to repeat the output in reverse order.
    references() #References for the code built.

# Iterates through each element in tuple to display an output that has 
# the value in a sentence.
def tuple_iterated(automobiles_tuple):
    for element in automobiles_tuple:
        print(f'{element} is one of many automobile brands.')
        print()

# Repeats the output in reverse order using a different context string.
def tuple_iterated_reversed(automobiles_tuple):
    for element in reversed(automobiles_tuple):
        print(f'Going through the tuple in reverse, {element} is one of '
              'many automobile brands.')
        print()

# An additional way to repeat the ouput in reverse order with a different context string.
def tuple_iterated_reversed_2(automobiles_tuple):
    for element in automobiles_tuple[-1::-1]:
        print(f'Another way to reverse the automobile tuple, the {element} brand is popular.')
        print()

# This is a function to list the cited reference for this program.
def references():
    print (f'\n\n\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()

if __name__ == "__main__":
    main()


    
    