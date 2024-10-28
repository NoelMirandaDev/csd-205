# Noel Miranda, July 11, 2024, Module 8.2 assignment.

# The purpose of this program is to familiarize oneself with dictionaries.
# This program initilizes a dictionary with 11 stocks. The dictionary
# has ticker symbols as the keys and the current price as the values. 
# There is a function for a user to search through the dictionary using 
# the keys to retrieve the price of a stock. If the ticker is not found, 
# there will be a message indicating the ticker was not found. 

def main():
    intro()
    # Dictionary for stocks tickers and prices.
    stocks = {'TSLA':'241.03', 'QS':'7.06', 'JOBY':'6.21', 'IWM':'210.68', 'META':'512.70', 'PEP':'163.95',
              'UBER':'73.53', 'JD':'28.63', 'AMT':'207.20', 'PFE':'28.66', 'POOL':'317.36'}
    # Searching through dictionary functionality
    while True:
        ticker = user_input() # User input
        if search_option(stocks, ticker):
            satisfied = input('Want to look for another ticker? "y" for yes or "n" for no. ')
        else:
            satisfied = input('The ticker symbol was not found, want to look for another? ' 
                         '"y" for yes or "n" for no. ')
        if satisfied.lower() == 'n':
            break

    print()
    # Imported references function for references of this code.
    references()

def intro():
    print()
    print('Welcome investor! We are a brokerage who has multiple options of stocks for you '
          'to invest in. Feel free to search for any stocks that you are interested in to see '
          'if it is part of our brokerage highly recommended investing stocks.')
    print()

# User ticker symbol input
def user_input():
    ticker = input('What is the ticker of the stock you are interested in? ')
    return ticker.upper()

# Search option for user to locate ticker and price within stock dictionary
def search_option(stocks, ticker):
    if ticker in stocks: 
        print(f'We have {ticker} at a current price of ${stocks[ticker]} per share.')
        return True 
    else:
        return False

# This is a function to list the cited reference for this program.
def references():
    print (f'\n\n\n***{'References':^50}***')
    print ('\nGaddis, T. (2022). Starting out with Python (6th ed.). Pearson.')
    print()
    
#Executes the main function when on the main program
if __name__ == '__main__':
    main()