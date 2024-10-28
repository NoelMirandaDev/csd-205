# Noel Miranda, May 31, 2024, Module 1.3 assignment.

# The purpose of this program is to calculate the 
# cost of installing fiber optic cable for any fictious company 

#Requests user's company's name in order to welcome them
company_name = input ("What is your company's name? ")
print ('Welcome ' + company_name + '! ') 

#Requests user's amount of feet needed
customer_response = input ('How many feet of fiber ' +
   'optic cable do you need installed ' + company_name + '? ')
requested_feet_of_fiber_optic = int (customer_response)

#Calculation to find out total cost of requested feet times price
Price_per_feet = .87
total_cost = float (requested_feet_of_fiber_optic * Price_per_feet)

#Displays total cost from calculation and a thank you message to company name.
print ('Thank you for your input ' + company_name + '.' +
       ' Your total cost for the requested number of ' +
       'feet of fiber optic cable installed is ' +
       f'${total_cost:.2f}.')

#Cited sources for this program
print (f'***{'Bibliography':^20}***')
print ('Gaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')

