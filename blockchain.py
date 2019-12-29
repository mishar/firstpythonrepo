# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain)  < 1:
        return None
        
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    """ This returns whatever the user inputs"""
    return (input("your choice was:"))


while True:
    print("Press 1 for input")
    print("Press 2 for output")
    print("Press q to quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_user_input()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        #output the blockchain list to the console
        for block in blockchain:
            print('outputting blocks')
            print(block)
    elif user_choice == 'q':
        break
    else:
        print("Wrong choice")
        continue

print('Done!')