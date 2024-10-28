# Noel Miranda, June 7, 2024, Module 2.2 assignment.
# The purpose of this program is to calculate the 
# cost of installing fiber optic cable for any fictious company with bulk
# discounts included.

# Requests user's company's name in order to welcome them
company_name = input ("What is your company's name? ")
print ('\nWelcome ' + company_name + ' to Fiber Optic Cable Incoporated! ') 

# Requests user's amount of feet needed
customer_response = input ('\nHow many feet of fiber ' +
   'optic cable do you need installed ' + company_name + '? ')
requested_feet = int (float(customer_response))

# Variable assignment for quantity of feet required for discount
DISCOUNT_A_ELIGIBILITY = 101 # 101 feet required for 7 cent bulk discount
DISCOUNT_B_ELIGIBILITY = 251 # 251 feet required for 17 cent bulk discount
DISCOUNT_C_ELIGIBILITY = 501 # 501 feet required for 37 cent bulk discount

# prices per foot depending on bulk discount eligibility
REGULAR_PRICE_PER_FOOT = .87
DISCOUNT_A_PRICE_PER_FOOT = .80
DISCOUNT_B_PRICE_PER_FOOT = .70
DISCOUNT_C_PRICE_PER_FOOT = .50

# Calculations to find out total cost of requested feet times price with bulk discount
# when applicable. Calculations displayed with if-else nested decision structure.
if requested_feet < DISCOUNT_A_ELIGIBILITY:
   total_cost = float (requested_feet * REGULAR_PRICE_PER_FOOT)
else:
   if requested_feet >= DISCOUNT_A_ELIGIBILITY and requested_feet < DISCOUNT_B_ELIGIBILITY:
      total_cost = float (requested_feet * DISCOUNT_A_PRICE_PER_FOOT)
   else:
       if requested_feet >= DISCOUNT_B_ELIGIBILITY and requested_feet < DISCOUNT_C_ELIGIBILITY:
          total_cost = float (requested_feet * DISCOUNT_B_PRICE_PER_FOOT)
       else: 
         requested_feet >= DISCOUNT_C_ELIGIBILITY
         total_cost = float (requested_feet * DISCOUNT_C_PRICE_PER_FOOT)

# Displays total cost from calculation and a thank you message to company name.
print (f'\nThank you for your input ' + company_name + '.' +
       f' Your total cost for', requested_feet ,
       f'feet of fiber optic cable installed is ' +
       f'${total_cost:,.2f}.')

# Cited sources for this program
print (f'\n\n\n***{'Resources':^50}***')
print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')

